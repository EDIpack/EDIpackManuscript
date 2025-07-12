# Import common Python modules
from itertools import product
import numpy as np

# Initialize the MPI library before creating the solver object
from mpi4py import MPI

# Import TRIQS many-body operator objects: annihilation, creation and
# occupation number operators
from triqs.operators import c, c_dag, n

# Import the solver object
from edipack2triqs.solver import EDIpackSolver

spins = ['up', 'dn']    # Names of spin projections
orbs = [0, 1, 2]        # List of impurity orbitals
bath_sites = [0, 1]     # List of bath sites, each carrying 3 orbitals

# Fundamental sets for impurity spin up/down degrees of freedom
fops_imp_up = [('up', orb) for orb in orbs]
fops_imp_dn = [('dn', orb) for orb in orbs]

# Fundamental sets for bath spin up/down degrees of freedom
# There are a total of 6 bath states for each spin projection
fops_bath_up = [('B_up', i) for i in range(3 * 2)]
fops_bath_dn = [('B_dn', i) for i in range(3 * 2)]

# Non-interacting part of the impurity Hamiltonian
h_loc = np.diag([-0.7, -0.5, -0.7])
H = sum(h_loc[o1, o2] * c_dag(spin, o1) * c(spin, o2)
        for spin, o1, o2 in product(spins, orbs, orbs))

# Interaction part
U = 3.0     # Local intra-orbital interactions U
Ust = 1.2   # Local inter-orbital interaction U'
Jh = 0.2    # Hund's coupling
Jx = 0.15   # Spin-exchange coupling constant
Jp = 0.1    # Pair-hopping coupling constant

H += U * sum(n('up', o) * n('dn', o) for o in orbs)
H += Ust * sum(int(o1 != o2) * n('up', o1) * n('dn', o2)
               for o1, o2 in product(orbs, orbs))

H += (Ust - Jh) * sum(int(o1 < o2) * n(s, o1) * n(s, o2)
                      for s, o1, o2 in product(spins, orbs, orbs))
H -= Jx * sum(int(o1 != o2) * c_dag('up', o1) * c('dn', o1) * c_dag('dn', o2) * c('up', o2)
              for o1, o2 in product(orbs, orbs))
H += Jp * sum(int(o1 != o2) * c_dag('up', o1) * c_dag('dn', o1) * c('dn', o2) * c('up', o2)
              for o1, o2 in product(orbs, orbs))

# Bath part

# Matrix dimensions of eps and V: 3 orbitals x 2 bath sites
eps = np.array([[-0.1, 0.1],
                [-0.2, 0.2],
                [-0.3, 0.3]])
V = np.array([[0.1, 0.2],
              [0.1, 0.2],
              [0.1, 0.2]])

# Dispersion of the bath states
H += sum(eps[o, nu] * c_dag("B_" + s, nu * 3 + o) * c("B_" + s, nu * 3 + o)
         for s, o, nu in product(spins, orbs, bath_sites))
# Coupling between the impurity and the bath
H += sum(V[o, nu] * (c_dag(s, o) * c("B_" + s, nu * 3 + o)
                     + c_dag("B_" + s, nu * 3 + o) * c(s, o))
         for s, o, nu in product(spins, orbs, bath_sites))

# Create a solver object
solver = EDIpackSolver(H, fops_imp_up, fops_imp_dn, fops_bath_up, fops_bath_dn)

# Solve the impurity model
beta = 100.0                 # Inverse temperature
n_iw = 1024                  # Number of Matsubara frequencies for GF calculations
energy_window = (-2.0, 2.0)  # Energy window for real-frequency GF calculations
n_w = 4000                   # Number of real-frequency points for GF calculations
broadening = 0.005           # Broadening on the real axis for GF calculations

solver.solve(beta=beta,
             n_iw=n_iw,
             energy_window=energy_window,
             n_w=n_w,
             broadening=broadening)

# On master MPI node, output some calculation results
if MPI.COMM_WORLD.Get_rank() == 0:
    # Print values of the static observables
    print("Potential energy:", solver.e_pot)
    print("Kinetic energy:", solver.e_kin)
    print("Densities (per orbital):", solver.densities)
    print("Double occupancy (per orbital):", solver.double_occ)

    # Use TRIQS' extensions to matplotlib to plot computed Green's functions
    from triqs.plot.mpl_interface import plt, oplot

    # Plot the Matsubara Green's functions (imaginary part)
    plt.figure(figsize=(4, 4))
    for orb in orbs:
        oplot(solver.g_iw['up'][orb, orb], mode='I',
              label=r"${\rm Im} G_" + str(orb) + r"(i\omega_n)$")
    plt.xlim((-3, 3))
    plt.ylabel(r"${\rm Im} G(i\omega_n)$")
    plt.legend()
    plt.savefig("G_iw.pdf")

    # Plot the orbital-resolved spectral functions
    plt.figure(figsize=(4, 4))
    for orb in orbs:
        oplot(solver.g_w['up'][orb, orb], mode='S', label=f"$A_%i(\\omega)$" % orb)
    plt.xlim(energy_window)
    plt.ylabel(r"$A(\omega)$")
    plt.legend()
    plt.savefig("A_w.pdf")

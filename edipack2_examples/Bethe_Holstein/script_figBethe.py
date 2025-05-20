import numpy as np
import matplotlib.image as image
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import pandas as pd
import sys
from matplotlib.colors import LinearSegmentedColormap
from scipy import optimize

def dens_bethe(x,d):
  root=(1-(x/d)**2)+0.j
  root=np.sqrt(root)
  dens_bethe=(2/(np.pi*d))*root
  return dens_bethe.real


W0_list = ["0.2","0.5","1.0","2.0","4.0","32.0","50.0","200.0","infty"]
W0_plot = np.float64(W0_list[:-1])
#W0_list = ["0.2","0.5","1.0","2.0","32.0","50.0","200.0","infty"]

plt.rcParams["font.family"] = "Times"
plt.rcParams['text.usetex'] = True
plt.rc('text.latex', preamble=r'\usepackage{amsmath,xcolor,amssymb,latexsym}')
plt.rcParams.update({'font.size': 40})
plt.rcParams['figure.figsize'] = [35, 10]


fig = plt.figure()
axs = plt.figure(layout="constrained").subplot_mosaic(
    """
    AB
    """
)


axs["A"].text(0.94, 0.04, r"(A)",transform=axs["A"].transAxes,fontsize=24, va='top', color='black')
axs["B"].text(0.94, 0.04, r"(B)",transform=axs["B"].transAxes,fontsize=24, va='top', color='black')





##################################################################
#Plot docc
ax=axs["A"]
n_docc_list=np.zeros(len(W0_list))
s_docc_list=np.zeros(len(W0_list))
print("Read Data docc...")
for iW,W0 in enumerate(W0_list):
  print("w0:",W0)
  n_docc_list[iW] = np.loadtxt(f'normal/W{W0}/observables_last.ed',unpack=True)[1]
  s_docc_list[iW] = np.loadtxt(f'superc/W{W0}/observables_last.ed',unpack=True)[1]

ax.set_xscale("log")
ax.set_xlabel(r'$\omega_0$/D')
ax.set_ylabel(r'$ \langle n_\uparrow n_\downarrow \rangle$')
ax.set_ylim(0.4,0.5)

ax.plot(W0_plot,n_docc_list[:-1],label="ed_mode=normal",c="orange",marker="o",linewidth=3)
ax.plot(W0_plot,s_docc_list[:-1],label="ed_mode=superc",c="red",marker="o",linewidth=3)
#AntiAdiabatic
ax.axhline(n_docc_list[-1],linestyle="--",c="orange",linewidth=6,alpha=.5)
ax.axhline(s_docc_list[-1],linestyle="--",c="red",linewidth=6,alpha=0.5)


ax.legend(loc='upper center') #, fontsize = '22', handlelength=1.5, framealpha=1)

##################################################################


#Plot phi_sc
ax=axs["B"]
s_phi_list=np.zeros(len(W0_list))
print("Read Data phi...")
for iW,W0 in enumerate(W0_list):
  print("w0:",W0)
  s_phi_list[iW] = abs(np.loadtxt(f'superc/W{W0}/phi_last.ed',unpack=True))

ax.set_xscale("log")
ax.set_xlabel(r'$\omega_0 /D$')
ax.set_ylabel(r'$ \phi $')


ax.plot(W0_plot,s_phi_list[:-1],label="ed_mode=superc",c="red",marker="o",linewidth=3)
#AntiAdiabatic
ax.axhline(s_phi_list[-1],linestyle="--",c="red",linewidth=6,alpha=0.5)


ax.legend(loc='lower center') #, fontsize = '22', handlelength=1.5, framealpha=1)

##################################################################


plt.savefig("figBethe_Holstein.pdf", bbox_inches='tight')

##################################################################
##################################################################
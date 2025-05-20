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



def zimS(x,z):
  y = (1.0-1.0/z)*x#-1/z*x
  return y


plt.rcParams["font.family"] = "Times"
plt.rcParams['text.usetex'] = True
plt.rc('text.latex', preamble=r'\usepackage{amsmath,xcolor,amssymb,latexsym}')
plt.rcParams.update({'font.size': 24})
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
ax=axs["A"]

print("Read Gimp")
gf = np.genfromtxt('w2d_cthyb/giw.dat',skip_header=0);x1=gf[:,0];y1=gf[:,2]
gf = np.genfromtxt('w2d_ed/giw.dat',skip_header=0)   ;x2=gf[:,0];y2=gf[:,2]
gf = np.genfromtxt('ed_for/impG_l11_s1_iw.ed',skip_header=0);x3=gf[:,0];y3=gf[:,1]

ax.set_xlim([0, 2])
ax.set_ylim([-2,0])
ax.set_xlabel(r'$\omega_n$')
ax.set_ylabel(r'${\rm Im}G(i\omega_n)$')
# ax.yaxis.set_tick_params(labelleft=False)
# ax.set_yticks([])

ax.tick_params(length=6, width=2,direction='out')
#ax.yaxis.grid(True, which='both', alpha=0.5)
#ax.yaxis.set_major_locator(mticker.LogLocator(base=10, numticks=10))

lw=5

ax.plot(x3,  y3, lw=lw, ls='solid',  c='black', marker='s', markersize=25, label=r"EDIpack", alpha=0.75)
ax.plot(x1,  y1, lw=lw, ls='',  c='red', marker='o', markersize=20, label=r"W2Dynamics CT-HYB", alpha=1.0, fillstyle='none', markeredgewidth=3)
ax.plot(x2,  y2, lw=lw, ls='',  c='green'  , marker='x', markersize=20, label=r"W2Dynamics EDIpack", alpha=1.0, fillstyle='none', markeredgewidth=3)


ax.legend(loc='upper center', fontsize = '22', handlelength=1.5, framealpha=1,ncol=6);
##################################################################





##################################################################
ax=axs["B"]
print("Read Data imSigma_iw")
gf = np.genfromtxt('w2d_cthyb/siw.dat',skip_header=0);x1=gf[:,0];y1=gf[:,2]
gf = np.genfromtxt('w2d_ed/siw.dat',skip_header=0)   ;x2=gf[:,0];y2=gf[:,2]
gf = np.genfromtxt('ed_for/impSigma_l11_s1_iw.ed',skip_header=0);x3=gf[:,0];y3=gf[:,1]

ax.set_xlim([0, 2])
ax.set_ylim([-0.6,0])
ax.set_xlabel(r'$\omega_n$')
ax.set_ylabel(r'${\rm Im}\Sigma(i\omega_n)$')
# ax.yaxis.set_tick_params(labelleft=False)
# ax.set_yticks([])

ax.tick_params(length=6, width=2,direction='out')
#ax.yaxis.grid(True, which='both', alpha=0.5)
#ax.yaxis.set_major_locator(mticker.LogLocator(base=10, numticks=10))

lw=5

ax.plot(x3,  y3, lw=lw, ls='solid',  c='black', marker='s', markersize=25, label=r"EDIpack", alpha=0.75)
ax.plot(x1,  y1, lw=lw, ls='',  c='red', marker='o', markersize=20, label=r"W2Dynamics CT-HYB", alpha=1.0, fillstyle='none', markeredgewidth=3)
ax.plot(x2,  y2, lw=lw, ls='',  c='green'  , marker='x', markersize=20, label=r"W2Dynamics EDIpack", alpha=1.0, fillstyle='none', markeredgewidth=3)

ax.legend(loc='upper center', fontsize = '22', handlelength=1.5, framealpha=1,ncol=6);
##################################################################





##################################################################
##################################################################
plt.savefig("figBetheW2D.pdf", bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
##################################################################
##################################################################

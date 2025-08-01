import numpy as np
import matplotlib.image as image
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import pandas as pd
import sys
from matplotlib.colors import LinearSegmentedColormap
from scipy import optimize
from mpl_toolkits.axes_grid1.inset_locator import inset_axes




plt.rcParams["font.family"] = "Times"
plt.rcParams['text.usetex'] = True
plt.rc('text.latex', preamble=r'\usepackage{amsmath,xcolor,amssymb,latexsym}')
plt.rcParams.update({'font.size': 30})
plt.rcParams['figure.figsize'] = [35, 15]


fig = plt.figure()
axs = plt.figure(layout="constrained").subplot_mosaic(
    """
    AABC
    """
)


axs["A"].text(0.02, 0.98, r"(A)",transform=axs["A"].transAxes,fontsize=24, va='top', color='black')
axs["B"].text(0.02, 0.98, r"(B)",transform=axs["B"].transAxes,fontsize=24, va='top', color='black')
axs["C"].text(0.02, 0.98, r"(C)",transform=axs["C"].transAxes,fontsize=24, va='top', color='black')



##################################################################
ax=axs["A"]

print("Read Data DOS")
rho1 = np.genfromtxt('U0.6/Gloc_i1_realw.dat',skip_header=0);x1=rho1[:,0];y1=-rho1[:,1]/np.pi
rho2 = np.genfromtxt('U1.0/Gloc_i1_realw.dat',skip_header=0);x2=rho2[:,0];y2=-rho2[:,1]/np.pi
rho3 = np.genfromtxt('U1.5/Gloc_i1_realw.dat',skip_header=0);x3=rho3[:,0];y3=-rho3[:,1]/np.pi
rho4 = np.genfromtxt('U2.0/Gloc_i1_realw.dat',skip_header=0);x4=rho4[:,0];y4=-rho4[:,1]/np.pi
rho5 = np.genfromtxt('U3.0/Gloc_i1_realw.dat',skip_header=0);x5=rho5[:,0];y5=-rho5[:,1]/np.pi
dos = np.genfromtxt('DOS2d.dat',skip_header=0);xdos=dos[:,0];ydos=dos[:,1]

ax.set_xlim([-2.5, 2.5])
ax.set_ylim([0.00, 12])
ax.set_xlabel(r'$\omega$')
ax.set_ylabel(r'$-{\rm Im}G_{loc}(\omega)/\pi$')
ax.yaxis.set_tick_params(labelleft=False)
ax.set_yticks([])

ax.tick_params(length=6, width=2,direction='out')

c = plt.cm.copper(np.linspace(0,1,5))
s = 2.0
lw=6

ax.plot(xdos  ,  ydos    ,  lw=4, ls='solid',  c="blue", alpha=0.5, label=r"$U=0.00$", zorder=2)
ax.plot(x1    ,  y1    ,  lw=lw, ls='solid',  c=c[0], label=r"$U=1.00$", zorder=1)
ax.plot(x2    ,  y2+1*s    ,  lw=lw, ls='solid',  c=c[1], label=r"$U=2.00$", zorder=1)
ax.plot(x3    ,  y3+2*s    ,  lw=lw, ls='solid',  c=c[2], label=r"$U=2.50$", zorder=1)
ax.plot(x4    ,  y4+3*s    ,  lw=lw, ls='solid',  c=c[3], label=r"$U=2.75$", zorder=1)
ax.plot(x5    ,  y5+4*s    ,  lw=lw, ls='solid',  c=c[4], label=r"$U=3.00$", zorder=1)

ax.legend(loc='upper center', fontsize = '28', handlelength=1, framealpha=1,ncol=3);
##################################################################





##################################################################
ax=axs["B"]
print("Read Data Delta VS u")
d1 = np.genfromtxt('phiVSu_dmft.dat',skip_header=0);x1=rho1[:,0];x1=d1[:,0];y1=d1[:,1]
d2 = np.genfromtxt('phiVSu_bcs.dat',skip_header=0);x2=rho2[:,0] ;x2=d2[:,0];y2=d2[:,1]


ax.set_xlim([0, 5])
ax.set_ylim([0, 0.6])
ax.set_xlabel(r'$U$')
ax.set_ylabel(r'$\phi$')
ax.tick_params(length=6, width=2,direction='out')



ax.plot(x2    ,  y2    ,  lw=10, ls='solid',  c='gray', alpha=0.5,label=r"BCS")
ax.plot(x1    ,  y1    ,  lw=5, ls='solid',marker='o', markersize=10, c='blue', label=r"DMFT")

ax.legend(loc='upper right', fontsize = '28', handlelength=1, framealpha=1,ncol=1);


# Create inset of width 30% and height 40% of the parent Axes' bounding box
# at the lower left corner.
axins = inset_axes(ax, width="60%", height="40%", loc="lower right")

print("Read Data Theta")
d1 = np.genfromtxt('CorrStrengthVSuloc.dat',skip_header=0);x1=d1[:,0];y1=d1[:,2]
## Move the x-axis tick labels to the top
axins.set_xlim([0, 5])
axins.set_ylim([0, 0.35])
axins.set_xlabel(r'$U$')
axins.set_ylabel(r'$\Theta$')
axins.tick_params(
    axis='x',         ## Apply changes to the x-axis
    top=True,         ## Show ticks on the top side
    labeltop=True,    ## Show tick labels on the top side
    bottom=False,     ## Hide ticks on the bottom side
    labelbottom=False ## Hide tick labels on the bottom side
    # length=6, width=2,direction='out'
)
axins.xaxis.set_label_position('top') 
axins.plot(x1    ,  y1    ,  lw=5, ls='solid',marker='s', markersize=10, c='green')


##################################################################




##################################################################
ax=axs["C"]
print("Read Data Phi vs T")
d1 = np.genfromtxt('phiVSbeta_dmft.dat',skip_header=0);x1=d1[:,0];y1=d1[:,1]
ax.set_xlim([0, 0.066])
ax.set_ylim([0, 0.52])
ax.set_xlabel(r'$T$')
ax.set_ylabel(r'$\phi$')
ax.tick_params(length=6, width=2,direction='out')

x=np.linspace(0.05,0.061,100)
y=3.2*np.sqrt(0.061-x)

ax.plot(1/x1    ,  y1    ,  lw=8, ls='solid', c='black')
ax.plot(x    ,  y    ,  lw=10, ls='dashed', c='red', alpha=0.5, label=r"$A\sqrt{T_c-T}$")

ax.legend(loc='lower left', fontsize = '28', handlelength=1, framealpha=1,ncol=1);
##################################################################







##################################################################
##################################################################
plt.savefig("figAHM.pdf", bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
##################################################################
##################################################################

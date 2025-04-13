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
    AABC
    """
)


axs["A"].text(0.94, 0.04, r"(a)",transform=axs["A"].transAxes,fontsize=24, va='top', color='black')
axs["B"].text(0.94, 0.04, r"(b)",transform=axs["B"].transAxes,fontsize=24, va='top', color='black')
axs["C"].text(0.94, 0.04, r"(c)",transform=axs["C"].transAxes,fontsize=24, va='top', color='black')





##################################################################
ax=axs["A"]

print("Read Data DOS")
rho1 = np.genfromtxt('U1.00/Gloc_realw.dat',skip_header=0);x1=rho1[:,0];y1=-rho1[:,1]/np.pi
rho2 = np.genfromtxt('U2.00/Gloc_realw.dat',skip_header=0);x2=rho2[:,0];y2=-rho2[:,1]/np.pi
rho3 = np.genfromtxt('U2.50/Gloc_realw.dat',skip_header=0);x3=rho3[:,0];y3=-rho3[:,1]/np.pi
rho4 = np.genfromtxt('U2.75/Gloc_realw.dat',skip_header=0);x4=rho4[:,0];y4=-rho4[:,1]/np.pi
rho5 = np.genfromtxt('U3.00/Gloc_realw.dat',skip_header=0);x5=rho5[:,0];y5=-rho5[:,1]/np.pi

dos=dens_bethe(x1,1.0)

ax.set_xlim([-3, 3])
ax.set_ylim([0.00, 4.25])
ax.set_xlabel(r'$\omega$')
ax.set_ylabel(r'$-{\rm Im}G(\omega)/\pi$')
ax.yaxis.set_tick_params(labelleft=False)
ax.set_yticks([])

ax.tick_params(length=6, width=2,direction='out')
#ax.yaxis.grid(True, which='both', alpha=0.5)
#ax.yaxis.set_major_locator(mticker.LogLocator(base=10, numticks=10))

c = plt.cm.copper(np.linspace(0,1,5))
s = 0.75

ax.plot(x1    ,  dos   ,  lw=5, ls='dashed', c='gray', label=r"$U=0.00$")
ax.plot(x1    ,  y1    ,  lw=5, ls='solid',  c=c[0], label=r"$U=1.00$")
ax.plot(x2    ,  y2+1*s    ,  lw=5, ls='solid',  c=c[1], label=r"$U=2.00$")
ax.plot(x3    ,  y3+2*s    ,  lw=5, ls='solid',  c=c[2], label=r"$U=2.50$")
ax.plot(x4    ,  y4+3*s    ,  lw=5, ls='solid',  c=c[3], label=r"$U=2.75$")
ax.plot(x5    ,  y5+4*s    ,  lw=5, ls='solid',  c=c[4], label=r"$U=3.00$")

ax.legend(loc='upper center', fontsize = '22', handlelength=1.5, framealpha=1,ncol=6);
##################################################################





##################################################################
ax=axs["B"]
print("Read Data imSigma_iw")
rho1 = np.genfromtxt('U1.00/impSigma_l11_s1_iw.ed',skip_header=0);x1=rho1[:,0];y1=rho1[:,1]
rho2 = np.genfromtxt('U2.00/impSigma_l11_s1_iw.ed',skip_header=0);x2=rho2[:,0];y2=rho2[:,1]
rho3 = np.genfromtxt('U2.50/impSigma_l11_s1_iw.ed',skip_header=0);x3=rho3[:,0];y3=rho3[:,1]
rho4 = np.genfromtxt('U2.75/impSigma_l11_s1_iw.ed',skip_header=0);x4=rho4[:,0];y4=rho4[:,1]
rho5 = np.genfromtxt('U3.00/impSigma_l11_s1_iw.ed',skip_header=0);x5=rho5[:,0];y5=rho5[:,1]


z1 = np.genfromtxt('U1.00/Z_last.ed',skip_header=0)
z2 = np.genfromtxt('U2.00/Z_last.ed',skip_header=0)
z3 = np.genfromtxt('U2.50/Z_last.ed',skip_header=0)
z4 = np.genfromtxt('U2.75/Z_last.ed',skip_header=0)


ax.set_xlim([0, 0.5])
ax.set_ylim([-4.5, 0])
ax.set_xlabel(r'$\omega$')
ax.set_ylabel(r'${\rm Im}\Sigma(i\omega)$')
ax.tick_params(length=6, width=2,direction='out')

c = plt.cm.copper(np.linspace(0,1,5))
xz = np.linspace(0,0.05,50)

ax.plot(x1    ,  y1    ,  lw=5, ls='solid',  c=c[0], label=r"$U=1.00$, $Z={:0.2f}$".format(z1))
ax.plot(x2    ,  y2    ,  lw=5, ls='solid',  c=c[1], label=r"$U=2.00$, $Z={:0.2f}$".format(z2))
ax.plot(x3    ,  y3    ,  lw=5, ls='solid',  c=c[2], label=r"$U=2.50$, $Z={:0.2f}$".format(z3))
ax.plot(x4    ,  y4    ,  lw=5, ls='solid',  c=c[3], label=r"$U=2.75$, $Z={:0.2f}$".format(z4))
ax.plot(x5    ,  y5    ,  lw=5, ls='solid',  c=c[4], label=r"$U=3.00$, ${\rm Im}\Sigma\simeq \tfrac{1}{\omega}$")


ax.plot(xz    ,  zimS(xz,z1)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)
ax.plot(xz    ,  zimS(xz,z2)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)
ax.plot(xz    ,  zimS(xz,z3)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)
ax.plot(xz    ,  zimS(xz,z4)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)


ax.legend(loc='lower left', fontsize = '22', handlelength=1, framealpha=1,ncol=1);
##################################################################



##################################################################
ax=axs["C"]
print("Read Data imSigma_w")
rho1 = np.genfromtxt('U1.00/impSigma_l11_s1_realw.ed',skip_header=0);x1=rho1[:,0];y1=rho1[:,2]
rho2 = np.genfromtxt('U2.00/impSigma_l11_s1_realw.ed',skip_header=0);x2=rho2[:,0];y2=rho2[:,2]
rho3 = np.genfromtxt('U2.50/impSigma_l11_s1_realw.ed',skip_header=0);x3=rho3[:,0];y3=rho3[:,2]
rho4 = np.genfromtxt('U2.75/impSigma_l11_s1_realw.ed',skip_header=0);x4=rho4[:,0];y4=rho4[:,2]
rho5 = np.genfromtxt('U3.00/impSigma_l11_s1_realw.ed',skip_header=0);x5=rho5[:,0];y5=rho5[:,2]


mask = (x1>-0.035) & (x1<0.035)
fit,cov = optimize.curve_fit(zimS,x1[mask],y1[mask],1)
z1=fit[0]
xz1 = np.linspace(x1[mask].min(), x1[mask].max(), 100)
yz1 = zimS(xz, z1)


xz = np.linspace(-0.035, 0.035, 50)

mask = (x2>-0.035) & (x2<0.035)
fit,cov = optimize.curve_fit(zimS,x2[mask],y2[mask],1);z2=fit[0]
yz2 = zimS(xz, z2)

mask = (x3>-0.035) & (x3<0.035)
fit,cov = optimize.curve_fit(zimS,x3[mask],y3[mask],1);z3=fit[0]
yz3 = zimS(xz, z3)

mask = (x4>-0.035) & (x4<0.035)
fit,cov = optimize.curve_fit(zimS,x4[mask],y4[mask],1);z4=fit[0]
yz4 = zimS(xz, z4)


ax.set_xlim([-0.2, 0.2])
ax.set_ylim([-0.53, 0.53])
ax.set_xlabel(r'$\omega$')
ax.set_ylabel(r'${\rm Re}\Sigma(\omega)$')
ax.tick_params(length=6, width=2,direction='out')

c = plt.cm.copper(np.linspace(0,1,5))


ax.plot(x1    ,  y1    ,  lw=5, ls='solid',  c=c[0], label=r"$U=1.00$, $Z={:0.2f}$".format(z1))
ax.plot(x2    ,  y2    ,  lw=5, ls='solid',  c=c[1], label=r"$U=2.00$, $Z={:0.2f}$".format(z2))
ax.plot(x3    ,  y3    ,  lw=5, ls='solid',  c=c[2], label=r"$U=2.50$, $Z={:0.2f}$".format(z3))
ax.plot(x4    ,  y4    ,  lw=5, ls='solid',  c=c[3], label=r"$U=2.75$, $Z={:0.2f}$".format(z4))
ax.plot(x5    ,  y5    ,  lw=5, ls='solid',  c=c[4], label=r"$U=3.00$")


ax.plot(xz    ,  zimS(xz,z1)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)
ax.plot(xz    ,  zimS(xz,z2)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)
ax.plot(xz    ,  zimS(xz,z3)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)
ax.plot(xz    ,  zimS(xz,z4)    ,  lw=8, ls='solid',  c='blue', alpha=0.3)


ax.legend(loc='lower left', fontsize = '22', handlelength=1, framealpha=1,ncol=1);
##################################################################





##################################################################
##################################################################
plt.savefig("figBethe.pdf", bbox_inches='tight')
plt.clf()
plt.cla()
plt.close()
##################################################################
##################################################################

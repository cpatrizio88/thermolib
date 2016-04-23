import site
import sys
site.addsitedir('/Users/cpatrizio/Dropbox/research/code/thermlib/')
import findTmoist
import findTmoist_new
from wsat import wsat
from constants import constants
import numpy as np
import thermo
import matplotlib.pyplot as plt

T_s = 302
p_s = 1000e2
p_t = 200e2
q_sat = wsat(T_s, p_s)
thetae0 = thermo.theta_e(T_s, p_s, q_sat, 0)

plevs = np.linspace(p_t, p_s, 1000)[::-1]

delp = np.diff(plevs)[0]


c = constants()

gamma_m = 6.5/1000. #lapse rate in K m^-1
gamma_d = 9.8/1000. #lapse rate in K m^-1

Tgm = np.zeros(plevs.shape)
Tgd = np.zeros(plevs.shape)

Tgm[0] = T_s
Tgd[0] = T_s

Tphumb =np.zeros(plevs.shape)
h = 7

gamma_ph = 6.2

zeta_levs = -h*np.log(plevs/p_s)
zeta_T = 16

for i, zeta in enumerate(zeta_levs):
    if (zeta < zeta_T):
      Tphumb[i] = T_s - gamma_ph*zeta
    else:
      Tphumb[i] = T_s - gamma_ph*zeta_T



Told = np.zeros(plevs.shape)
Tnew = np.zeros(plevs.shape)

for i, p in enumerate(plevs[:-1]):
    Tgm[i+1] = Tgm[i]*(1 + gamma_m*c.Rd*delp/p)
    Tgd[i+1] = Tgd[i]*(1+ gamma_d*c.Rd*delp/p)
    Told[i] = findTmoist.findTmoist(thetae0, p)
    Tnew[i] = findTmoist_new.findTmoist(thetae0, p, q_sat, 0)

   

    
    

plt.figure(1)
plt.plot(Told[:-1], plevs[:-1]/100., color='r', label='Told - root finder moist adiabat')
plt.plot(Tnew[:-1], plevs[:-1]/100., color='b', label='Tnew - root finder moist adiabat')
plt.plot(Tgm[:-1], plevs[:-1]/100., 'g--', label='constant gamma_m')
plt.plot(Tgd[:-1], plevs[:-1]/100., 'k--', label='constant gamma_d')
plt.plot(Tphumb, plevs/100., color ='y', label='pierre humbert profile')
plt.legend()
#plt.gca().invert_yaxis()
plt.show()
    





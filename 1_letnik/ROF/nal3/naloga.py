import scipy
import numpy as np
import matplotlib.pyplot as plt
#-----------------------------DATASTORAGE-----------------------------#

#vhodni podatki

tstart = 0
tend = 20

RE = 6378100
X = 0
Y = 100000 + RE

deg = 45
ini_v = 11111
phi = deg * np.pi / 180

vx = ini_v * np.cos(phi)
vy = ini_v * np.sin(phi)

#interval [0, 20] razdeli na 5000 delov
t = np.linspace(tstart,tend,5000)

#Variable za simuliranje spremembe r0 skozi cas

KONS_G = 3.9860188*10**(26)
KONS_RHO = KONS_G * 5.314*10**(-23) / (300 * 1.380649*10**(-23))
KA = 1 #k/m

"""
print(ini_v, phi, vx, vy)
print("----------------")
print(KONS_G, KONS_RHO)
"""

#-----------------------------PODNALOGA A-----------------------------#

def path(t, w, KONS_G, KONS_RHO, KA, RE):
    x,y = w
    return [KONS_G/(x**2+y**2)* (x/(y*np.sqrt(x**2/y**2 + 1))) + KA*vx * 1.293* np.exp(KONS_RHO*(1/np.sqrt(x**2+y**2) + 1/RE)) , KONS_G/(x**2+y**2)* (np.sqrt(x**2/y**2 + 1)) + KA*vy * 1.293* np.exp(KONS_RHO*(1/np.sqrt(x**2+y**2) + 1/RE))]

sol1 = scipy.integrate.solve_ivp(path, [tstart, tend], [vx,vy], t_eval = t, args=(KONS_G, KONS_RHO, KA, RE), dense_output=True)

w = sol1.sol(t)
plt.plot(sol1.t, w.T[:,0], '-', c = 'red', label='s(t)')
plt.plot(sol1.t, w.T[:,1], '-', c = 'blue', label='i(t)')
plt.plot(sol1.t, w.T[:,2], '-', c = 'purple', label='r(t)')

plt.title("S, I, R : primer A")
plt.xlabel("Time")
plt.ylabel("Število ljudi")

plt.legend()
plt.grid()
plt.show()

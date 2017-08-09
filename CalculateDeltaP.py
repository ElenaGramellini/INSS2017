###############################
###      Important notes    ###
### the v is in mm/microsec ###
### the E is in V/cm       ###
###############################

import argparse
import math

def DeltaP(mass):
    m2 = mass*mass
    m4 = m2*m2

    mMu  = 105.6583745 
    mPi  = 139.57018
    mMu2 = mMu*mMu
    mPi2 = mPi*mPi

    D2MuPi2 = mPi2 - mMu2
    S2MuPi2 = mPi2 + mMu2

    Num = D2MuPi2*D2MuPi2
    Den = Num - 2*m2*S2MuPi2 + m4
    DeltaP = math.sqrt(Num/Den) - 1
    return DeltaP



import matplotlib.pyplot as plt
import numpy as np

fig1 = plt.figure(facecolor='white')
t1 = np.arange(0.01, 1.0, 0.001)
f2 = np.vectorize(DeltaP)
line1 = plt.semilogx(t1, f2(t1),label="DeltaP",linewidth=2.0)

plt.grid(True)
plt.title('Sensitivity to Neutrino Mass in Pion Decay at Rest')
plt.xlabel('Muon Neutrino Mass [MeV]')
plt.ylabel('$\Delta$p / p')
plt.show()






#plt.plot(t1, E2v(t1,87), 'bo')



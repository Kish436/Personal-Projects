import numpy as np
import matplotlib.pyplot as plt

def BrownianMotion(t, nSteps, nPaths):
    dt=t/nSteps
    steps=np.random.choice([-np.sqrt(dt),np.sqrt(dt)], size=(nPaths, nSteps))
    W=np.cumsum(steps, axis=1)
    W=np.hstack([np.zeros((nPaths,1)), W])
    T=np.linspace(0,t,nSteps+1)
    return T,W

t,W=BrownianMotion(1,1000,1)
plt.plot(t,W.T)
plt.xlabel('Time')
plt.ylabel('W Transposed')
plt.title('Brownian Motion')
plt.show()



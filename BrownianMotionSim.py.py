import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def BrownianMotion(t, nSteps, nPaths):
    dt=t/nSteps
    steps=np.random.choice([-np.sqrt(dt),np.sqrt(dt)], size=(nPaths, nSteps))
    W=np.cumsum(steps, axis=1)
    W=np.hstack([np.zeros((nPaths,1)), W])
    T=np.linspace(0,t,nSteps+1)
    return T,W

def GBM(t, nSteps, nPaths, S0, mu, sigma):

    t,W=BrownianMotion(1,1000,1)
    St = S0*np.exp((mu-0.5*sigma**2)*t+sigma*W)
    return t, St

T,S = GBM(t=1, nSteps=1000, nPaths=5, S0=100, mu=0.08, sigma=0.2)
plt.plot(T,S.T)
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Geometric Brownian Motion')
plt.show()







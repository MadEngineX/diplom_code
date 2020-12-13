import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def approximate(x, y):
    def func(t, A, h, T, phi):
        return A*np.exp(-h*t)*np.sin(2*np.pi/T*t + phi)

    t = np.array(x)
    y = np.array(y)

    popt, pcov = curve_fit(func, t, y, (1e3, 1e-2, 1., -1e1), maxfev=10**6)
    A, h, T, phi = popt
    plt.scatter(t, y, s=30, color='orange')
    plt.plot(t, func(t, *popt))
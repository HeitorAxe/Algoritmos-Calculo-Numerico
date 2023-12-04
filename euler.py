import numpy as np
import matplotlib.pyplot as plt

def euler_method(f, t0, tn, y0, h):
    n = int((tn - t0) / h) + 1
    t = np.linspace(t0, tn, n)
    y = np.zeros_like(t)
    y[0] = y0
    
    for i in range(1, n):
        y[i] = y[i-1] + h * f(t[i-1], y[i-1])
    
    return t, y

def population_growth(t, P):
    r = 0.02
    return r * P

t, P = euler_method(population_growth, 0, 10, 100, 0.1)

plt.plot(t, P)
plt.xlabel('Tempo')
plt.ylabel('População')
plt.title('Crescimento Populacional')
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
def feval(funcName, *args):
    return eval(funcName)(*args)
def RK4Ordem(func, yinit, x_range, h):
    m = len(yinit)
    n = int((x_range[-1] - x_range[0])/h)
    x = x_range[0]
    y = yinit
    xsol = np.empty(0)
    xsol = np.append(xsol, x)
    ysol = np.empty(0)
    ysol = np.append(ysol, y)
    for i in range(n):
        k1 = h*feval(func, x, y)
        k2 = h*feval(func, x+h/2, y + k1*(h/2))
        k3 = h*feval(func, x+h/2, y + k2*(1/2))
        k4 = h*feval(func, x+h, y + k3)
        for j in range(m):
            y[j] = y[j] + (1/6)*(k1[j] + 2*k2[j] + 2*k3[j] + k4[j])
        x = x + h
        xsol = np.append(xsol, x)
        for r in range(len(y)):
            ysol = np.append(ysol, y[r])
    return [xsol, ysol]
    2
def myFunc(x, y):
    dy = np.zeros((len(y)))
    dy[0] = 4*x- 2*x*y
    return dy
# -----------------------h bem pequeno

h = 0.2
x = np.array([0.0, 2.0])
yinit = np.array([1.0])
[ts, ys] = RK4Ordem('myFunc', yinit, x, h)
dt = int((x[-1]-x[0])/h)
t = [x[0]+i*h for i in range(dt+1)]
yexact = []
for i in range(dt+1):
    ye = 2 - 1*np.exp(-t[i]*t[i])
    yexact.append(ye)
difere = ys - yexact
print("Diferença máxima =", np.max(abs(difere)))
plt.plot(ts, ys, 'r')
plt.plot(t, yexact, 'b')
plt.xlim(x[0], x[1])
plt.legend(["RK de 4a ordem", "Solução Exata"], loc=2)
plt.xlabel('x', fontsize=17)
plt.ylabel('y', fontsize=17)
plt.tight_layout()
plt.show()
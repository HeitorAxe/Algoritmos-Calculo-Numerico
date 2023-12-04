import numpy as np
import matplotlib.pyplot as plt

# Função que representa a equação diferencial
def f(x, y):
    return y/x - (y/x)**2

# Solução analítica
def analytical_solution(x):
    return x / (1 + np.log(x))

# Método de Runge-Kutta de quarta ordem para resolver o PVI
def runge_kutta_4th_order(f, x0, y0, h, x_end):
    x_values = [x0]
    y_values = [y0]

    while x_values[-1] < x_end:
        x = x_values[-1]
        y = y_values[-1]

        k1 = h * f(x, y)
        k2 = h * f(x + 0.5*h, y + 0.5*k1)
        k3 = h * f(x + 0.5*h, y + 0.5*k2)
        k4 = h * f(x + h, y + k3)

        y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6

        x_values.append(x + h)
        y_values.append(y_new)

    return np.array(x_values), np.array(y_values)

# Parâmetros do problema
x0 = 1
y0 = 1
x_end = 3

# Valores de h a serem testados
hs = [0.25, 0.1, 0.05]

# Plotagem da solução analítica e soluções aproximadas
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)

x_analytical = np.linspace(x0, x_end, 100)
y_analytical = analytical_solution(x_analytical)
plt.plot(x_analytical, y_analytical, label='Solução Analítica', linestyle='--')

for h in hs:
    x_values, y_values = runge_kutta_4th_order(f, x0, y0, h, x_end)
    plt.plot(x_values, y_values, label=f'Runge-Kutta (h={h})', marker='o')

plt.title('Soluções do PVI usando o Método de Runge-Kutta')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Cálculo dos erros e plotagem
plt.subplot(1, 2, 2)

for h in hs:
    x_values, y_values = runge_kutta_4th_order(f, x0, y0, h, x_end)
    analytical_values = analytical_solution(x_values)
    errors = np.abs(y_values - analytical_values)
    plt.plot(x_values, errors, label=f'Erro (h={h})', marker='o')

plt.title('Erro em função de x para diferentes valores de h')
plt.xlabel('x')
plt.ylabel('Erro')
plt.legend()

plt.tight_layout()
plt.show()

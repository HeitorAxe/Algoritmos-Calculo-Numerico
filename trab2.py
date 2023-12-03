import numpy as np

def funcao_exemplo1(x):
    return np.exp(-x**2)

def funcao_exemplo2(x):
    return np.log(x + np.sqrt(x + 1))

def regra_trapezios(f, a, b, n):
    h = (b - a) / n
    integral_aproximada = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        integral_aproximada += f(a + i * h)
    
    integral_aproximada *= h
    return integral_aproximada

def regra_simpson(f, a, b, n):
    h = (b - a) / n
    integral_aproximada = f(a) + f(b)

    for i in range(1, n, 2):
        integral_aproximada += 4 * f(a + i * h)
    
    for i in range(2, n-1, 2):
        integral_aproximada += 2 * f(a + i * h)
    
    integral_aproximada *= h / 3
    return integral_aproximada

def calcular_integral_com_precisao(f, a, b, precisao):
    n = 1
    integral_anterior = 0
    integral_atual_trapezios = regra_trapezios(f, a, b, n)
    integral_atual_simpson = regra_simpson(f, a, b, n)

    while abs(integral_atual_trapezios - integral_anterior) > precisao:
        n *= 2
        integral_anterior = integral_atual_trapezios
        integral_atual_trapezios = regra_trapezios(f, a, b, n)
        integral_atual_simpson = regra_simpson(f, a, b, n)

    return integral_atual_trapezios, integral_atual_simpson, n

def gerar_tabela(f, a, b, n):
    tabela = []
    h = (b - a) / n

    for i in range(n + 1):
        x = a + i * h
        y = f(x)
        tabela.append((x, y))

    return tabela

# Definindo o intervalo de integração
a = 0
b = 1

# Calculando a integral para a primeira função: e^(-x^2)
print("Resultados para a função e^(-x^2):")
precisao = 1e-3
integral_trapezios, integral_simpson, particionamento = calcular_integral_com_precisao(funcao_exemplo1, a, b, precisao)
print(f"Integral (∫e^(-x^2)dx) usando a Regra dos Trapézios: {integral_trapezios}")
print(f"Integral (∫e^(-x^2)dx) usando a Regra de Simpson: {integral_simpson}")

# Gerando a tabela para a primeira função
tabela1 = gerar_tabela(funcao_exemplo1, a, b, particionamento)

# Calculando a integral para a segunda função: ln(x + √(x+1))
print("\nResultados para a função ln(x + √(x+1)):")
integral_trapezios, integral_simpson, particionamento = calcular_integral_com_precisao(funcao_exemplo2, a, b, precisao)
print(f"Integral (∫ln(x + √(x+1))dx) usando a Regra dos Trapézios: {integral_trapezios}")
print(f"Integral (∫ln(x + √(x+1))dx) usando a Regra de Simpson: {integral_simpson}")

# Gerando a tabela para a segunda função
tabela2 = gerar_tabela(funcao_exemplo2, a, b, particionamento)

# Apresentando a tabela para a primeira função
print("\nTabela de Pontos para a função e^(-x^2) (xi, yi):")
print("   x          y")
for ponto in tabela1:
    print(f"{ponto[0]:.4f}   {ponto[1]:.4f}")

# Apresentando a tabela para a segunda função
print("\nTabela de Pontos para a função ln(x + √(x+1)) (xi, yi):")
print("   x          y")
for ponto in tabela2:
    print(f"{ponto[0]:.4f}   {ponto[1]:.4f}")

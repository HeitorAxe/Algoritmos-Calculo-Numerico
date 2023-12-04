from math import *

# define a função f(x)
def f(x):
  return x**3 + x**2 - 3*x - 12

# define os extremos do intervalo

inf = int(input("Digite o limite inferior do intervalo onde a raiz será procurada: "))
sup = int(input("Digite o limite superior do intervalo onde a raiz será procurada: "))

print(f"Intervalo escolhido: [{inf}, {sup}]")

# a tolerância indica o quão próximo a aproximação está da raiz
TOL = 0.001

if f(inf)*f(sup) < 0:           # verifica se há raiz nesse intervalo (se f(a) e f(b) forem positivo/negativo, f(a)*f(b) será negativo)
    med = (inf+sup)/2           # encontra o ponto médio do intervalo
    while abs(f(med)) > TOL:    # o loop para quando atinge a tolerância
        if f(inf)*f(med) < 0:   # Teorema de Bolzano
            sup = med           # atualiza os extremos do intervalo
            med = (inf+sup)/2
        else:
            inf = med
            med = (inf+sup)/2
    print(f"Raiz encontrada: {med}")                # a raiz foi encontrada
else:
    print("Não pode-se afirmar que há raiz nesse intervalo")
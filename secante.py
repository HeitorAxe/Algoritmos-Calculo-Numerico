def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        
        if abs(f_x1) < tol:
            return x1
        
        if abs(f_x1 - f_x0) < tol:
            raise Exception("O método da secante falhou devido a uma possível divisão por zero.")
        
        x_next = x1 - (f_x1 * (x1 - x0)) / (f_x1 - f_x0)
        
        if abs(x_next - x1) < tol:
            return x_next
        
        x0 = x1
        x1 = x_next

    raise Exception("O método da secante atingiu o número máximo de iterações.")

# Exemplo de uso:
def f(x):
    return x**3 - 4*x - 9

x0 = 1.0
x1 = 3.0
tolerance = 1e-6

root = secant_method(f, x0, x1, tol=tolerance)
print("A raiz aproximada é:", root)
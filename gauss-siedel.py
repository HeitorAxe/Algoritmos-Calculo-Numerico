import numpy as np

def gauss_siedel(A, B, initial_guess, tol=1e-6, max_iter=100):
    n = len(B)
    x = initial_guess.copy()
    
    for iter_count in range(max_iter):
        for i in range(n):
            x[i] = (B[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]

        if np.linalg.norm(np.dot(A, x) - B) < tol:
            return x

    raise Exception("O método de Gauss-Siedel atingiu o número máximo de iterações.")

# Exemplo de uso:
A = np.array([[10, 2, 1],
              [1, 5, 1],
              [2, 3, 10]])

B = np.array([7, -8, 6])

initial_guess = np.zeros(len(B))

solutions = gauss_siedel(A, B, initial_guess)
print("As soluções são:", solutions)

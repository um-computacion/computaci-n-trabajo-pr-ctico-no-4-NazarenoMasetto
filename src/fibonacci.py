def fibonacci_iterative(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma iterativa.

    """
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no está definida para negativos.")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursive(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma recursiva.

    
    """
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no está definida para negativos.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

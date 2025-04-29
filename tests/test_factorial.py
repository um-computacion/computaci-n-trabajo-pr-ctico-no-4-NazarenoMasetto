def factorial_iterative(n):
    """
    Calcula el factorial de un número de forma iterativa.
    
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def factorial_recursive(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

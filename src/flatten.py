def flatten(data):
    """
    Aplana listas, tuplas y diccionarios anidados.

    """
    resultado = []

    if isinstance(data, (list, tuple)):
        for elemento in data:
            resultado.extend(flatten(elemento))
    elif isinstance(data, dict):
        for clave, valor in data.items():
            resultado.extend(flatten(clave))
            resultado.extend(flatten(valor))
    else:
        resultado.append(data)

    return resultado

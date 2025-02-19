def calcular_area_rectangulo(longitud, ancho):
    """
    Calcula el área de un rectángulo.

    Args:
        longitud: La longitud del rectángulo.
        ancho: El ancho del rectángulo.

    Returns:
        El área del rectángulo.
    """
    if not isinstance(longitud, (int, float)):
        raise TypeError("La longitud debe ser un número.")
    if not isinstance(ancho, (int, float)):
        raise TypeError("El ancho debe ser un número.")
    if longitud < 0 or ancho < 0:
        raise ValueError("La longitud y el ancho deben ser positivos.")
    return longitud * ancho


#def calcular_area_rectangulo(longitud, ancho):
    """
    Calcula el área de un rectángulo (intencionalmente incorrecto).
    """
    if not isinstance(longitud, (int, float)):
        raise TypeError("La longitud debe ser un número.")
    if not isinstance(ancho, (int, float)):
        raise TypeError("El ancho debe ser un número.")
    if longitud < 0 or ancho < 0:
        raise ValueError("La longitud y el ancho deben ser positivos.")
    return longitud - ancho  # cambien el codigo, esto  debería ser longitud * ancho


#Este error intencional habría causado que las pruebas test_area_cero y test_area_positiva 
#fallaran, ya que la función ya no calcula el área correctamente.
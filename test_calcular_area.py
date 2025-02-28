import math

def calcular_area_rectangulo(longitud, ancho):
    if not isinstance(longitud, (int, float)) or not isinstance(ancho, (int, float)):
        raise TypeError("Los valores deben ser números.")
    if longitud < 0 or ancho < 0:
        raise ValueError("Los valores deben ser positivos.")
    return longitud * ancho

def calcular_area_circulo(radio):
    if not isinstance(radio, (int, float)):
        raise TypeError("El radio debe ser un número.")
    if radio < 0:
        raise ValueError("El radio debe ser positivo.")
    return math.pi * radio ** 2

def calcular_area_triangulo(base, altura):
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("Los valores deben ser números.")
    if base < 0 or altura < 0:
        raise ValueError("Los valores deben ser positivos.")
    return (base * altura) / 2

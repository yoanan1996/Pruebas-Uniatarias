import unittest  # Importa el módulo unittest para crear pruebas unitarias
from Calcular_area import calcular_area_rectangulo  # Importa la función a probar

class TestCalcularAreaRectangulo(unittest.TestCase):
    """
    Esta clase contiene las pruebas unitarias para la función calcular_area_rectangulo.
    Hereda de unittest.TestCase para acceder a las herramientas de testing.
    """

    def test_area_positiva(self):
        """
        Prueba el cálculo del área con entradas positivas válidas.
        Verifica si la función devuelve el resultado correcto para entradas positivas.
        """
        self.assertEqual(calcular_area_rectangulo(5, 10), 50)  # Afirma que el resultado es 50

    def test_area_cero(self):
        """
        Prueba el cálculo del área cuando uno de los lados es cero.
        Verifica si la función devuelve 0 cuando uno de los lados es cero.
        """
        self.assertEqual(calcular_area_rectangulo(0, 10), 0)  # Afirma que el resultado es 0

    def test_area_negativa(self):
        """
        Prueba qué sucede cuando se proporcionan entradas negativas.
        Verifica si la función lanza una excepción ValueError cuando se le dan entradas negativas.
        """
        with self.assertRaises(ValueError):  # Espera que la función lance una excepción ValueError
            calcular_area_rectangulo(-5, 10)  # Llama a la función con entradas negativas

    def test_area_tipos_incorrectos(self):
        """
        Prueba qué sucede cuando se proporcionan entradas de tipos incorrectos.
        Verifica si la función lanza una excepción TypeError cuando se le dan entradas de tipos incorrectos.
        """
        with self.assertRaises(TypeError):  # Espera que la función lance una excepción TypeError
            calcular_area_rectangulo("5", 10)  # Llama a la función con entradas de tipos incorrectos

if __name__ == '__main__':
    unittest.main()  # Ejecuta las pruebas unitarias si el script se ejecuta directamente
    
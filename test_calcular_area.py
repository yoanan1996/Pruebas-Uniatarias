import unittest
from Calcular_area import calcular_area_rectangulo, calcular_area_circulo, calcular_area_triangulo

class TestCalculoAreas(unittest.TestCase):

    def test_area_rectangulo(self):
        self.assertEqual(calcular_area_rectangulo(5, 10), 50)
        self.assertEqual(calcular_area_rectangulo(0, 10), 0)
        with self.assertRaises(ValueError):
            calcular_area_rectangulo(-5, 10)

    def test_area_circulo(self):
        self.assertAlmostEqual(calcular_area_circulo(7), 153.93804002589985)
        self.assertEqual(calcular_area_circulo(0), 0)
        with self.assertRaises(ValueError):
            calcular_area_circulo(-3)

    def test_area_triangulo(self):
        self.assertEqual(calcular_area_triangulo(4, 6), 12)
        self.assertEqual(calcular_area_triangulo(0, 10), 0)
        with self.assertRaises(ValueError):
            calcular_area_triangulo(-5, 10)

if __name__ == '__main__':
    unittest.main()

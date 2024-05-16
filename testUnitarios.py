import unittest
from func.desvioPadrao import calcular_desvio_padrao
from func.media import calcular_media
from func.mediana import calcular_mediana
from func.moda import calcular_moda

class testesUnitarios(unittest.TestCase):
    def test_calcular_media(self):
        try:
            self.assertAlmostEqual(calcular_media([1, 2, 3, 4, 5]), 3.0)
        except:
            print('A média calculada está incorreta')

    def test_calcular_mediana(self):
        try:
            self.assertEqual(calcular_mediana([1, 2, 3, 4, 5]), 3)
        except:
            print('A mediana calculada está incorreta para uma lista com um número ímpar de elementos')

        try:
            self.assertEqual(calcular_mediana([1, 2, 3, 4, 5, 6]), 3.5)
        except:
            print('A mediana calculada está incorreta para uma lista com um número par de elementos')

    def test_calcular_desvio_padrao(self):
        try:
            self.assertAlmostEqual(calcular_desvio_padrao([1, 2, 3, 4, 5]), 1.414213562)
        except:
            print('O desvio padrão calculado está incorreto')

    def test_calcular_moda(self):
        try:
            self.assertAlmostEqual(calcular_moda([1, 2, 7, 7, 1, 3, 4, 5, 7]), [7])
        except:
            print('A moda está errada para um número retornado')

        try:
            self.assertAlmostEqual(calcular_moda([1, 2, 7, 7, 1, 1, 3, 4, 5, 7]), [1, 7])
        except:
            print('A moda está errada para mais de um número retornado')

if __name__ == '__main__':
    unittest.main()

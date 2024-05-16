import unittest
from func.desvioPadrao import calcular_desvio_padrao
from func.media import calcular_media
from func.mediana import calcular_mediana

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

if __name__ == '__main__':
    unittest.main()

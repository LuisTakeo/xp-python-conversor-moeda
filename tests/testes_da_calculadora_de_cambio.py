from unittest import TestCase
import src.calculadora_de_cambio as calc

class TestesDaCalculadoraDeCambio(TestCase):

    def teste_conversao_cambio_valor_0_taxa_5_03_retorna_0(self):
        # Arrange
        valor = 0
        taxa = 3.37
        resultado_esperado = 0

        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_1_taxa_5_17_retorna_0_19(self):
        # Arrange
        valor = 1
        taxa = 5.17
        iof = (100 - 1.1) / 100
        resultado_esperado = round(valor / taxa * iof, 2)

        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_negativo_retorna_0(self):
        # Arrange
        valor = -1
        taxa = 5.17
        resultado_esperado = 0

        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)

    def teste_conversao_cambio_valor_1000_taxa_5_56_retorna_179_85(self):
        # Arrange
        valor = 1000
        taxa = 5.56
        iof = (100 - 1.1) / 100
        resultado_esperado = round(valor / taxa * iof, 2) - 1

        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)
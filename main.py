import src.calculadora_de_cambio as calc

print("Cotacao de valores")
valor = float(input("Insira o valor em reais: "))
selecaoTaxa = int(input("Digite 1 para dolar, 2 para euro: "))
taxa = 0
moeda = ''
if (selecaoTaxa == 1):
	taxa = 5.17
	moeda = 'dollar'
if (selecaoTaxa == 2):
	taxa = 5.56
	moeda = 'euro'
if (taxa >= 0):
	resultado = calc.converter(valor, taxa)
	resultadoTexto = f"O resultado da cotacao e de {resultado} "
	print(resultadoTexto)

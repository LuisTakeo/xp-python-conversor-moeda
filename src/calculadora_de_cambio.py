import math

def converter(valor, taxa):
    if (valor <= 0):
        return 0
    iof = (100 - 1.1) / 100
    valor_cambio = round(valor / taxa * iof, 2)
    return valor_cambio
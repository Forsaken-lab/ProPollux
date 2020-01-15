"""
Conversor de moeda (Real para Dolar), considerando um dolar a R$ 3.27
Author: André Protasio Version: 0.0.1 Date: Jan/2020
"""
cotação = float(input('Qual a cotação atual do dolar?: R$'))

reais = float(input('Qual valor deseja converter: R$'))

dolar = reais / 3.27

print('Com R${} você pode comprar US${:.2f}'.format(reais, dolar))

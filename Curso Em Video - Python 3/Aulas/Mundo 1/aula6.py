"""
    Tipos Primitivos
inteiro (int) - Flutuante(float) -  boleano(bool) - Texto(str)
"""
print('Calculadora de soma')
num1 = int(input('Escreva o primeiro numero '))
num2 = int(input('Escreva o segundo numero '))

r = num1 + num2
print("A soma ente {} e {} tem o resultado de {}.".format(num1,num2,r))

#comando tipe() é para saber o tipo da variavel
print(type(num1))

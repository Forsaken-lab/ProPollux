#Operadores aritimeticos
"""
5+2==7      adição
5-2==3      Subtração
5*2==10     Multiplicação
5/2==2.5    Divisão
5**2==25    Potenciação
5//2==2     Divisão Inteira
5%2==1      Divisão Modulo (Resto da divisão)
"""
#Ordem de precedência
"""
1- [] (Para expresoes aritimeticas o python só utiliza parenteses)
2- **
3- *, /, //, %
4- +, -

nome = input('Qual é o seu nome?\n')
print('Seu nome é {}'.format(nome))
print('Seu nome é {:>20}'.format(nome))
print('Seu nome é {:<20}'.format(nome))
print('Seu nome é {:^20}'.format(nome))
print('Seu nome é {:=^20}'.format(nome))
"""
n1 = int(input('Escreva um numero \n'))
n2 = int(input('Escreva o segundo numero \n'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e =n1 ** n2
print('A soma é de {}\n A Multiplicação é de {}\n A divisão é de {:.3f}'.format(s, m, d))
print('A divisão inteira é de {}\n A exponenciação é de {}'.format(di, e))
"""
Desafio 
005 Receba um valor e mostrar o valor anterior e o posterior
006 Criar um algoritomo que mostre o dobro o triplo e raiz quadrada de um numero
007 Desenvol um programa que calcule uma media de acordo com 2 notas de um aluno
008 Programa que converta metros para centimetros e milimetros
009 Ler um numero inteiro e mostrar a tabuada
010 Ler quanto dinheiro a pessoa tem e quantos dolares ela pode comprar (1 Dolar = R$ 3,27)
011 Leia a autura e larguar de uma parede e mostrar quanto de tinta precisa pra pintar sabendo que 1 Litro pinta 2m Quadrados
012 Leia o preço de um produto e mostrar o novo preço com 5% de desconto
013 Faça um algoritimo que calcule o salario de uma pessoa mais 15% de almento
"""
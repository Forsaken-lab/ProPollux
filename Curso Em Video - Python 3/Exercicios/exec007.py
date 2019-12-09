#Calculo de media - v0.1
#Author: André Protasio Date:2019/Dez
nome = str(input('Escreva o nome do aluno:\n'))
nota1 = float(input('Escreva a primeira nota:\n'))
nota2 = float(input('Escreva a segunda nota:\n'))
media = (nota1 + nota2) / 2
print('O aluno {} teve a nota {} e nota {} e sua media é de {:.2f} como nota geral.'.format(nome, nota1, nota2, media))

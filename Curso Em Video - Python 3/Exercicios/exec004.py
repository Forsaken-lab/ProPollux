# Exec 004 - curso python - mostrar informaçoes (tipos primitivo)
a = input('Escreva algo e tenha uma surpressa \n')
print('O que voce escreveru é ')
print('Número? : {} \n Texto? : {} \n Maiusculas? : {} \n Minusculas? : {} \n Indetificavel? : {}'.format(a.isnumeric(), a.isalpha(), a.isupper(),a.islower(),a.isidentifier()))

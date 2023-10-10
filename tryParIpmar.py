numero=input('digite um número inteiro: ')
print(numero)
try:
    numero_int=int(numero)
    par_impar=numero_int%2==0
    par_impar_texto='ímpar'
    if par_impar:
        par_impar_texto='par'
    print(f'O número {numero_int} é {par_impar_texto}.')
except:
    print('Não digitou número inteiro.')
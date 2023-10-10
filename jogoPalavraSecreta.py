print('-='*30)
print(f'FORCA')
print('-='*30)
tentativa=0
palavra_secreta='abobrinha'
letra_acertada=''
while True:
    letra_digitada=input('Digite uma letra: ').strip().lower()
    tentativa+=1
    if len(letra_digitada)>1:
        if letra_digitada==palavra_secreta:
            print('PARABÉNS!! Você acertou.')
            break
        else:
            print('Digite apenas uma letra.')
            continue
    if letra_digitada in palavra_secreta:
        letra_acertada+=letra_digitada
    palavra_formada=''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada+=letra_secreta
        else:
            palavra_formada+='*'
    print(f'Palavra formada: {palavra_formada}')
    if palavra_formada==palavra_secreta:
        print('PARABÉNS!! Você acertou.')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Foram {tentativa} tentativa(s).')
print(letra_acertada)
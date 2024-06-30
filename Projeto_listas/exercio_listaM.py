import Vnumeros, registro_media
cores = {'quebra': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m'}
contagem_num = media = quebra = 0
lista_numeros = []
mudar = ''
dlista = False
while True:
    res = ''
    numero = Vnumeros.verificacao()  # Chama função para quant de números e a verif se é inteiro!
    if numero == 0:
        break
    else:
        lista = Vnumeros.cadastro(numero)  # add os números na lista!
        lista_numeros.append(lista[:])  # Add em cópia em uma nova lista!
        lista.clear()
    if len(lista_numeros) == 1:  # Faz a média se for a primeira
        for cont in range(0, len(lista_numeros[0])):
            contagem_num += lista_numeros[0][cont]
        media = contagem_num / len(lista_numeros[0])
    else:
        contagem_v = 0  # Faz a média se for a 2º ou maior!
        for i, v in enumerate(lista_numeros):
            for cont in v:
                contagem_v += 1
                contagem_num += cont
        media = contagem_num / contagem_v
    contagem_num = 0
    registro_media.medias(media)
    print(f'{cores['verde']}A media da lista digitada foi:{cores['quebra']} {cores['vermelho']}'
          f'{media:.2f}{cores['quebra']}')  # Mostra a média de todas lista feitas!
    while True:
        try:
            res = str(input(f'{cores['vermelho']}Deseja continuar ?{cores['quebra']} [S/N]: ')).upper()[0]
        except KeyboardInterrupt:
            print(f'{cores['vermelho']}O Usuario preferiu encerrar o programa!{cores['quebra']}')
            quebra = 1
            break
        if res == 'S':
            print('-'*30)
            print('Selecione as opções:')
            print(f'{cores['vermelho']}1º continuar na mesma lista:')
            print(f'2º mudar a lista:')
            print(f'3º Mostrar médias ja cadastradas{cores['quebra']}:')
            mudar = Vnumeros.numeroverificado()  # verificação se continua na lista ou apaga!
            if mudar == 1:
                break
            elif mudar == 2:
                lista_numeros.clear()
                break
            else:
                registro_media.monstarmedias()
        elif res == 'N':
            break
        else:
            print(f'{cores['vermelho']}O parametro digitado está errado! tente novamente{cores['quebra']}')
    if res == 'N' or quebra == 1 or mudar == 0:
        break
print(f'{cores['vermelho']}PROGRAMA FINALIZADO!!{cores['quebra']}')

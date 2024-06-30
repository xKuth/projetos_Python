cores = {'quebra': '\033[m', 'vermelho': '\033[31m', 'verde': '\033[32m'}


def verificacao():
    """
    -> Verificar a Quant de valores na mesma lista!
    :return: Quantidade de números que deseja em um mesmo indice na lista
    """
    while True:
        try:
            numero = str(input(f'{cores['verde']}Quantos números você quer a média? {cores['quebra']}'))
            if numero == '0':
                print(f'{cores['vermelho']}0 não é aceito nessa operação!{cores['quebra']}')
            elif numero.isnumeric():
                numero = int(numero)
                return numero
        except (TypeError, ValueError):
            print(f'{cores['vermelho']}Valor digitado não é inteiro ou não é númerico!'
                  f' Tente novamente{cores['quebra']}')
        except KeyboardInterrupt:
            print()
            print(f'{cores['vermelho']}O ÚSUARIO PREFERIU ENCERRAR O PROGRAMA{cores['quebra']}')
            return 0

def cadastro(numero):
    """
    -> Faz o cadastro de números inteiros em uma lista!
    :param numero: Quantidade de números que seram adicionados!
    :return: Todos números cadastros em uma lista!
    """
    lista = []
    while True:
        print('Quais número deseja adicionar? ')
        for cont in range(0, numero):
            try:
                quant = str(input(f'{cont+1}º: '))
                if quant.isnumeric():
                    quant = int(quant)
                    lista.append(quant)
            except KeyboardInterrupt:
                print(f'{cores['vermelho']}O USUARIO DECIDIU ENCERRAR O PROGRAMA!{cores['quebra']}')
                break
            except (ValueError, TypeError):
                print(f'{cores['vermelho']}valor passado invalido! tente novamente.{cores['quebra']}')
        return lista


def numeroverificado():
    """
    -> Verificação se é pra apagar a lista ou para mante-la
    :return: opção selecionada (1 ou 2)
    """
    while True:
        try:
            valor = str(input(f'{cores['verde']}digite o valor [1 / 2 / 3]: {cores['quebra']}')).strip()
            if valor.isnumeric() and valor == '1' or '2' or '3':
                num = int(valor)
                return num
            else:
                print('Valor não correspondente')
        except (ValueError, TypeError):
            print(f'{cores['vermelho']}O valor verificado não corresponde a inteiro! Tente novamente{cores['quebra']}')
        except KeyboardInterrupt:
            print()
            print(f'{cores['vermelho']}O usuario decidiu encerrar o programa!{cores['quebra']}')
            return 0

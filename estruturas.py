''' # ESTRUTURAS # '''

''' CONDICIONAL '''
def estruturaCondicional():
    nome = 'Bruno'
    if nome == 'Guilherme':
        print('O nome não é Guilherme.')
    elif nome == 'Laura':
        print('O nome não é Laura.')
    else:
        print('O nome é Bruno.')

''' REPETIÇÃO '''
def estruturaRepeticao():
    lista_compras = ['Arroz', 'Feijão', 'Banana', 'Carnes', 'Refrigerante']
    # Fazer um for in para listar todos os itens da lista
    print('LISTA DE COMPRAS (for in): ')
    for compra in lista_compras:
        print(compra)
    # O while irá executar o bloco indentado em loop até que a condição seja cumprida.
    aux = 5
    while aux != 5:
        print('Este é um while.')
        aux -= 1

''' EXCEÇÕES '''
# Funciona como um try exception do Java
def estruturaTryExcept():
    # Finally: sempre executado. Independente se houver ou não a exception
    try:
        num = int(input('Informe um número inteiro: '))
    except ValueError:
        print('Valor incorreto.')
    else:
        print(f'Você digitou {num}')
    finally:
        print("Sempre sou executado.")

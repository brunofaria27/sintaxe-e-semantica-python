''' # TIPOS # '''

''' FLOAT E INT '''
def typeIntFloat():
    number_int = 1
    number_float = 2.14
    print(f'Tipo de number_int = {type(number_int)}')
    print(f'Tipo de number_float = {type(number_float)}')

''' STRING '''
def typeString():
    name = 'Linguagens de Programação' # Palavra escrita entre aspas quer dizer String
    # Uso de Slice em Python (de tal indice até tal indice)
    print(f'Slice da palavra {name} de 0:8 -> {name[0:5]}')
    # Pode ser utilizado para ler a String ao contrário também
    print(f'Slice da palavra {name} de 0::-1 -> {name[0::-1]}')
    

''' BOOLEAN '''
def typeBool():
    a = True
    b = False
    print(f'Tipo de a = {type(a)}')
    print(f'Tipo de b = {type(b)}')
    print(f'AND em a e b = {a and b}')
    print(f'OR em a e b = {a or b}')

''' LIST '''
def typeList():
    list_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print(list_numbers)
    print(f'Tipo de list_numbers -> {type(list_numbers)}')
    # Substituir elementos dentro de uma lista
    list_numbers[0] = 155
    print(f'Após alteração a lista fica {list_numbers}')

''' TUPLE '''
def typeTuple():
    print(f'Criação e mostra de duas tuplas:')
    tupla1 = (1, 2, 3, 4, 5, 6)
    print(tupla1)
    print(type(tupla1))
    tupla2 = 1, 2, 3, 4, 5, 6
    print(tupla2)
    print(type(tupla2))
    # Desempacotamento de Tupla
    # Gera ValueError se colocar um numero diferente de elementos para desempacotar.
    print(f'\nDesempacotamento de tuplas:')
    tupla3 = ('PUC Minas', "Linguagens de programação")
    escola, curso = tupla3
    print(escola)
    print(curso)
    # Metódos de adição e remoção em tuplas não existem, dado o fato de tuplas serem imutáveis.
    # Soma*, procurar valor max* e min*, tamanho
    # Se os valores forem todos inteiros ou reais
    print(f'\nMetódos das tupals:')
    tupla4 = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(sum(tupla4)) # soma
    print(max(tupla4)) # máximo valor
    print(min(tupla4)) # minimo valor
    print(len(tupla4)) # tamanho lista
    # Concatenação de Tuplas
    print(f'Concatenação de tuplas:')
    tupla7 = 1, 2, 3
    tupla8 = 4, 5, 6
    print(tupla7)
    print(tupla8)
    print(tupla7 + tupla8)
    tupla7 = tupla7 + tupla8
    print(tupla7) # Tuplas são imutaveis mas podemos sobrescrever seus valores

''' DICT '''
def typeDict():
    # Criação de dicionários
    # Forma 1 (Mais comum):
    print(f'Criação de dicionários (Forma mais comum): ')
    paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'pt': 'Portugal'}
    print(paises)
    print(type(paises))
    # Forma 2 (Menos comum):
    print(f'\nCriação de dicionários (Forma menos comum): ')
    paises2 = dict(br='Brasil', eua='Estados Unidos', pt='Portugal')
    print(paises2)
    print(type(paises2))
    # Pegando itens de um dicionário
    print(f'\nPegando itens de um dicionário: ')
    print(f'Pegando país de chave br = ' + str(paises['br']))
    # Podemos utilizar
    print(f'Pegando pais usando .get = ' + str(paises.get('eua')))

''' SET '''
def typeSet():
    # O tipo set é inferido com uma lista de elementos separados por vírgulas, e entre chaves {}.
    nomes_set = {'bruno', 'guilherme', 'laura'}
    # O tipo frozenset (set imutável) é inferido com a função frozenset(), recebendo um array de elementos.
    sobrenomes_set = frozenset(['faria', 'dantas', 'xavier'])
    print(f'Nomes: {nomes_set}')
    print(f'Sobrenomes: {sobrenomes_set}')
    # Verificando se alguns intens estão nos sets
    print(f'Amanda esta em nomes_set? ' + str({'amanda' in nomes_set}))
    print(f'Ochoa esta em nomes_set? ' + str({'ochoa' in sobrenomes_set}))
    # Pode ser feito a unição de dois sets sem repetir valores
    print(f'nomes_set.union(sobrenomes_set) -> ' + str(nomes_set.union(sobrenomes_set)))
    # Mostrando os itens que não estão contidos em um e em outro
    print(f'nomes_set.difference(sobrenomes_set)' + str(nomes_set.difference(sobrenomes_set)))

''' COMPLEX '''
def typeComplex():
    # Tipo complexo é inferido com a atribuição de um número complexo (num real + num imaginario)
    # Número imáginario e acompanhado por um 'j'
    complex1 = 5 + 2j
    # Pode-se utilizar a função complex()
    complex2 = complex(10, 4)
    print("complex1 = 5 + 2j")
    print("complex2 = complex(10, 4)")
    print("complex1 == complex2 = " + str(complex1 == complex2))
    print("complex1 = " + str(complex1))
    print(type(complex1))
    print("complex1.real = " + str(complex1.real)) # Imprimindo o número real
    print("complex1.imag = " + str(complex1.imag)) # Imprimindo o número imaginário

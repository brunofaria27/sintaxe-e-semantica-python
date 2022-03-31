import sys

''' # REFERENCE COUNTING # '''
# Tem o intuito de mostrar quantas vezes determinado objeto é apontado no programa
# Isso é necessário para o Garbage Collector desalocar a variável quando não tiver mais referências
def referenceCouting():
    x = 100
    y = x # Referència para x
    z = x # Referència para x
    w = x # Referència para x
    print(f'Números de referências presentes em x = {sys.getrefcount(x)}')

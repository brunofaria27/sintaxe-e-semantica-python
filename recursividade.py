''' # RECURSIVIDADE # '''

''' CONTAGEM DECREMENTAL '''
def decremental():
    value = int(input('Digite um valor que deseja decrementar: '))
    recursiveDecremental(value)

def recursiveDecremental(value):
    if value == 0: # Caso o valor recebido seja 100, a recursão será parada.
        print('Terminou!')
    else:
        # Eventualmente, n chegará a 100 e a recursão será interrompida.
        print('Valor atual = ' + str(value))
        recursiveDecremental(value - 1)

''' FIBONACCI '''
def recursiveFibonacci(n):
    if n <= 1: # Caso n <= 1
        return n # Retorna n, encerrando o loop
    else:
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2)

def fibonacci():
    terms = int(input("Inserir um numero positivo: "))
    print("Sequência de Fibonacci = ")
    for i in range(terms): # Realizar a recursão n vezes, obtendo n termos da sequência de Fibonacci
        print(recursiveFibonacci(i), end=' ')


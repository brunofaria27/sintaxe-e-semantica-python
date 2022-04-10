# Import da biblioteca de Thread que executa em concorrencia mais de uma tarefa
import threading as th

# Função da Tarefa 1
def tarefa1():
    X = 0
    while X <= 10:
        print('Tarefa 1')
        X += 1

# Função da Tarefa 2
def tarefa2():
    Y = 0
    while Y <= 10:
        print('Tarefa 2')
        Y += 1

# Colocar em Thread a Função 1 e 2 para serem executadas ao mesmo tempo
def executar():
    print('\nCOM THREAD')
    th.Thread(target=tarefa1).start()
    tarefa2()

def executarSemThread():
    print('\nSEM THREAD')
    tarefa1()
    tarefa2()
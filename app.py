# IMPORTS DE DIRETÓRIOS
import paradigmas
import estruturas
import recursividade
import reference_couting
import tipos

# IMPORTS PARA O PROGRAMA
import os
import time
from colorama import Fore, Back, Style
from pyfiglet import figlet_format

''' # PROGRAMA PRINCIPAL # '''
# Função utilizada para mostrar o menu para usuário
def menu():
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print(figlet_format('OPTIONS', font="standard"))
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print('[1] - Paradigmas')
    print('[2] - Estruturas')
    print('[3] - Recursividade')
    print('[4] - Tipos')
    print('[5] - Reference Couting')
    print('[0] - Sair')

# Função utilizada para mostrar o menu de funções dos paradigmas
def paradigmasMenu():
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print(figlet_format('PARADIGMAS', font="standard"))
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print('[1] - Paradigma Imperativo')
    print('[2] - Paradigma Funcional')
    print('[3] - Paradigma Orientado a Objetos')
    print('[4] - Paradigma Procedural')

# Função utilizada para mostrar o menu de funções das estruturas
def estruturasMenu():
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print(figlet_format('ESTRUTURAS', font="standard"))
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print('[1] - Estruturas Condicional')
    print('[2] - Estruturas Repetição')
    print('[3] - Estruturas de Exceções')

# Função utilizada para mostrar o menu de funções da recursividade
def recursividadeMenu():
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print(figlet_format('RECURSIVIDADE', font="standard"))
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print('[1] - Recursividade Contagem Decremental')
    print('[2] - Recursividade Fibonacci')

# Função utilizada para mostrar o menu de funções dos tipos
def tiposMenu():
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print(figlet_format('TIPOS', font="standard"))
    print(Fore.CYAN + "==========================================================================" + Style.RESET_ALL)
    print('[1] - Tipo INT e FLOAT')
    print('[2] - Tipo STRING')
    print('[3] - Tipo BOOLEAN')
    print('[4] - Tipo LIST')
    print('[5] - Tipo DICIONÁRIO')
    print('[6] - Tipo TUPLE')
    print('[7] - Tipo SET')
    print('[8] - Tipo COMPLEX')

# Interação com o usuário
aux = -1

while aux != 0:
    menu()
    aux = int(input("Digite uma opção que deseja: "))
    print('Aguarde 3 segundos...')
    time.sleep(3)
    os.system('clear') or None
    if aux == 1:
        try:
            paradigmasMenu()
            option = int(input('Digite a opção desejada: '))
            print('Aguarde 3 segundos...')
            time.sleep(3)
        except:
            print('Erro na hora de pegar seleção paradigmas')
    
        if option == 1:
            print('\n* EXEMPLO PARADIGMA IMPERATIVO *')
            paradigmas.imperativoParadigma()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 2:
            print('\n* EXEMPLO PARADIGMA FUNCIONAL *')
            paradigmas.funcionalParadigma()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 3:
            print('\n* EXEMPLO PARADIGMA ORIENTADO A OBJETOS *')
            paradigmas.PooParadigma()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 4:
            print('\n* EXEMPLO PARADIGMA PROCEDURAL *')
            paradigmas.proceduralParadigma()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        else:
            print('Valor inválido...')
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
    elif aux == 2:
        try:
            estruturasMenu()
            option = int(input('Digite a opção desejada: '))
            print('Aguarde 3 segundos...')
            time.sleep(3)
            os.system('clear') or None
        except:
            print('Erro na hora de selecionar função de estruturas...')

        if option == 1:
            print('\n* EXEMPLO ESTRUTURA CONDICIONAL *')
            estruturas.estruturaCondicional()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 2:
            print('\n* EXEMPLO ESTRUTURA DE REPETIÇÃO *')
            estruturas.estruturaRepeticao()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 3:
            print('\n* EXEMPLO ESTRUTURA DE EXCEÇÕES *')
            estruturas.estruturaTryExcept()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        else: 
            print('Valor inválido...')
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
    elif aux == 3:
        try:
            recursividadeMenu()
            option = int(input('Digite a opção desejada: '))
            print('Aguarde 3 segundos...')
            time.sleep(3)
            os.system('clear') or None
        except:
            print('Erro na seleção de função de recursividade')

        if option == 1:
            print('\n* EXEMPLO RECURSIVIDADE CONTAGEM DECREMENTAL *')
            recursividade.decremental()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 2:
            print('\n* EXEMPLO RECURSIVIDADE FIBONACCI *')
            recursividade.fibonacci()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        else:
            print('Valor inválido...')
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
    elif aux == 4:
        try:
            tiposMenu()
            option = int(input('Digite a opção desejada: '))
            print('Aguarde 3 segundos...')
            time.sleep(3)
            os.system('clear') or None
        except:
            print('Erro na hora de seleção de funções de tipos em Python.')

        if option == 1:
            print('\n* EXEMPLO TIPO FLOAT E INT *')
            tipos.typeIntFloat()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 2:
            print('\n* EXEMPLO TIPO STRING *')
            tipos.typeString()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 3:
            print('\n* EXEMPLO TIPO BOOLEAN *')
            tipos.typeBool()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 4:
            print('\n* EXEMPLO TIPO LIST *')
            tipos.typeList()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 5:
            print('\n* EXEMPLO TIPO DICIONÁRIO *')
            tipos.typeDict()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 6:
            print('\n* EXEMPLO TIPO TUPLE *')
            tipos.typeTuple()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 7:
            print('\n* EXEMPLO TIPO SET *')
            tipos.typeSet()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        elif option == 8:
            print('\n* EXEMPLO TIPO COMPLEX *')
            tipos.typeComplex()
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
        else:
            print('Valor inválido...')
            input('\nPressione ENTER para continuar...')
            os.system('clear') or None
    elif aux == 5:
        os.system('clear') or None
        print('\n* EXEMPLO REFERENCE COUNTING *')
        reference_couting.referenceCouting()
        input('\nPressione ENTER para continuar...')
        os.system('clear') or None
    else: 
        aux = 0
        print('Obrigado por utilizar o nosso programa...')
        time.sleep(3)

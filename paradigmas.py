import sys

''' # PARADIGMAS # '''

''' IMPERARTIVO '''
# O paradigma imperativo deve ser capaz de dar instruções ao computador.
# Ou seja, baseado em lista de comandos que alteram um estado (váriavel)
def imperativoParadigma():
    number = int(input("Digite um número: "))
    print(f'O número {number} foi declarado.')
    number += 15
    print(f'Foi acrescentado 15 ao valor digitado: {number}')

''' FUNCIONAL '''
# O paradigma funcional consiste em utilizar funções como na matemática
# Ou seja, mapeamento de entradas e saídas sem um efeito colateral
def funcMath(value):
    return value ** 3 + 4 * 10 * value

def funcionalParadigma():
    number = int(input("Digite um número: "))
    result = funcMath(number)
    print(f'Passando o valor {number} na equação (x^3 + 4 * 10 * x) resulta no valor: {result}')

''' ORIENTADO A OBJETO '''
# Estrutura em módulos (classes) que agrupam um estado (atributo) e operações (metódos) sobre esse estado
class venda:    # Criação da classe venda
    def __init__(self, nome, venda, valor): # Construtora da classe venda (initializer)
        self.nome = nome
        self.venda = venda
        self.valor = valor
        # Todos objetos da classe recebem o self que aponta para o objeto instanciado que invocou.
        # Depois, serão recebidos os valores que serão colocados nos atributos da classe.

    # Metódo utilizado para listar todas as vendas criadas.
    def listarVendas(self):
        print(f'Vendedor: {self.nome}')
        print(f'Código de venda: {self.venda}')
        print(f'Valor da venda: {self.valor}')

def PooParadigma():
    # Criação de objetos
    venda_carlos = venda('Carlos', '#124', 1200.99)
    venda_pedro =  venda('Pedro', '#146', 25999.99)
    print("Mostrando as vendas criadas: ")
    # Chamada das funções da classe
    venda_carlos.listarVendas()
    venda_pedro.listarVendas()

''' PROCEDURAL '''
# O paradigma procedural consiste em chamar funções que desviam a execução do código.
# Ou seja, temos maior controle do fluxo do programa porque ele é escrito em funções.
def CHAMADA():
    print(f'Fui chamada!')

def proceduralParadigma():
    number_1 = 10
    print(f'A cada alteração na variável number_1, vamos chamar a função CHAMADA()!')
    number_1 += 10
    print(f'Valor number_1 = {number_1}')
    CHAMADA()
    number_1 += 100
    print(f'Valor number_1 = {number_1}')
    CHAMADA()
    number_1 *= 5
    print(f'Valor number_1 = {number_1}')
    CHAMADA()


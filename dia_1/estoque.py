from datetime import datetime
from produto import Produto
from lista_dados import produtos_de_mercado
import time
import random
from faker import Faker
# A classe é como a arquitura, a planta baixa da casa, que cada um dos nossos objetos que serão criados 
# irão seguir, ele possuirão cada um deles um loca que será preenchido com informações próprias previamente 
# específicadas na classe, chamados atributos, também cada objeto possuirá métodos próprios que manimulam 
# os atributos ou informações internas, manipulam as informações daquele objeto singular. 

class Estoque:

    # Método dunder (double underscore) que é chamado quando o nome da classe é declarado, no caso Estoque, 
    # e este método cria espaços na memória para armazenar os objetos e seus atributos, e pode receber argumentos 
    # que podem ser atribuídos aos atributos dos objetos. 

    def __init__(self, tipo= None):

        # Privando os atributos para definirmos a lógica de encapsulamento. 

        # Este atributo armazenará objetos produto. 
        self.__produtos = []

        # Quando cada estoque for criado nós teremos o registro de tempo. 

        self.__data_criacao = datetime.now()

        self.__tipo = tipo

    # Encapsulamento

    # Getters, a lógica de leitura. 
    @property 
    def produtos(self):

        # Definindo uma lógica de leitura.
        return self.__produtos

    @property 
    def data_criacao(self):
        return self.__data_criacao

    @property 
    def tipo(self):
        return self.__tipo 

    

    def adicionar_produto(self, robo= None, nome= None, custo= None, lucro= None, imposto= None, quantidade= None, validade= None):

        # nome = input("Indique ") 

        if robo == False: 

            def adicionado_produtos():

                quantidade_adicionar = int(input("Indique a quantidade de produtos que você gostaria de adicionar: "))

                produtos_adicionados = 0 
                while produtos_adicionados < quantidade_adicionar: 

                    nome = input("Indique o nome do produto: ")

                    print()

                    custo = float(input("Indique o custo do produto: "))

                    print()
                    lucro = float(input("indique a margende lucro: "))

                    print()
                    imposto = int(input("Indique a quantidade de imposto que será paga (em porcentagem): "))

                    print()
                    quantidade = int(input("Indique a quantidade de unidades que você irá adicionar deste produto: "))

                    print()
                    validade = int(input("Indique a quantidade de meses que esse produto ainda será válido: "))

                    # Futuramente irei criar uma classe produtos, 
                    # por enquanto estou apenas testando. 

                    produto_a = Produto(nome, custo, lucro, imposto, quantidade, validade)

                    self.__produtos.append(produto_a)

                    time.sleep(1)
                    print("Produto adicionado com sucesso!")

                    # produtos_adicionados = produtos_adicionados + 1 

                    produtos_adicionados += 1

            try: 

                adicionado_produtos()

            except TypeError as msg: 
                print(msg)
                print("A quantidade de produtos a adicionar deve ser indicada \n utilizando um tipo inteiro de dados!")
                time.sleep(2)
                print("...")
                time.sleep(2)
                print("Tentando novamente!")

                adicionado_produtos()


        else: 

            produto_a = Produto(nome, custo,lucro, imposto, quantidade, validade)

            self.__produtos.append(produto_a)






# estoque_1 = Estoque("Calçados")

# print("Tipo do Estoque:", estoque_1.tipo)
# print("Produtos:", estoque_1.produtos)
# print("Data de Criação do Estoque:", estoque_1.data_criacao) 

# estoque_1.adicionar_produto()

# print("Produtos: " + str(estoque_1.produtos))

# lista_produtos = estoque_1.produtos

# print("Produtos Criados: ")
# for produto in lista_produtos: 
#     print(produto)


# # tempo_agora = datetime.timestamp(1)
# tempo = datetime.now()

# # print("Tempo agora: ", tempo_agora)
# print("Tempo: ", tempo)


estoque_1 = Estoque("Supermecado.")

# estoque_1.adicionar_produto()


# for produto in estoque_1.produtos:

#     print(produto.nome)

faker = Faker('pt_BR')

def criar_produtos(produtos_nomes):



    for numero in range(0, 100): 

        random.shuffle(produtos_nomes)
        nome = random.choice(produtos_nomes)
        marca = faker.name_male()
        custo = random.uniform(0.99, 15.95)


        lucro = random.randint(10, 50)
        imposto = random.randint(20, 30)
        quantidade = random.randint(10, 200)
        validade = random.randint(30, 120)


        estoque_1.adicionar_produto(True, nome, custo, lucro, imposto, quantidade, validade)


def mostrar_produtos(objeto_estoque):

    produtos_mostrados = 0
    indice = 0
    while produtos_mostrados < len(objeto_estoque.produtos):

        print(f"""Nome: {objeto_estoque.produtos[indice].nome}""")

        indice += 1 
        produtos_mostrados += 1


criar_produtos(produtos_de_mercado)

mostrar_produtos(estoque_1)
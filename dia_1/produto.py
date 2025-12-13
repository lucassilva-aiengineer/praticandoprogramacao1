# Criando uma classe produto, destinada ao design dos próximos produtos. 
from datetime import datetime, timedelta

class Produto:

    def __init__(self, nome, custo, lucro, imposto, quantidade, validade):

        # Privando os atributos para que eles não sejam acessados de forma pública. 

        self.__nome = nome 
        self.__custo = custo 
        self.__lucro = lucro
        self.__imposto = imposto
        self.__quantidade = quantidade
        self.__validade = datetime.now() + timedelta(days= validade) 
        self.__data_criacao = datetime.now()


    # Definindo a regra de leitura, no caso por enquanto teremos uma regra de leitura 
    # simples bem parecida com a leitura de um atributo público. 

    # Atributos privados métodos públicos. 

    # Getters 
    @property 
    def nome(self):
        return self.__nome 

    @property 
    def custo(self):

        # Utilizamos o self para acessar os atributos do próprio objeto, bem parecido com o
        # que fazemos com objetos que já foram criados. 

        return self.__custo

    @property 
    def lucro(self):
        return self.__lucro

    @property
    def quantidade(self):
        return self.__quantidade

    @property 
    def imposto(self):

        # senha = int(input("Digite a sua senha: "))

        # if senha == 1234:
        #     return self.__validade 

        # else:
        #     return "Acesso negado!"

        return self.__imposto

    @property 
    def validade(self):
        return self.__validade 


    @property
    def data_criacao(self):
        return self.__data_criacao 


    # Setters 
    # Desenvolvendo a nossa regra ed escrita. 

    @nome.setter 
    def nome(self, novo_nome):
        self.__nome = novo_nome


    @custo.setter 
    def custo(self, novo_custo):
        self.__custo = novo_custo 


    @custo.setter 
    def lucro(self, novo_lucro):
        self.__lucro = novo_lucro


    @quantidade.setter 
    def quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade 


    @imposto.setter 
    def imposto(self, novo_imposto):
        self.__imposto = novo_imposto


    @validade.setter
    def validade(self, nova_validade):
        self.__validade 


    @data_criacao.setter 
    def data_criacao(self, nova_data):
        self.__data_criacao = nova_data



# produto_1 = Produto("Refrigerante", 10.99, 5, 10)


# validade_do_produto = produto_1.validade

# print(validade_do_produto) 

# print(produto_1.)



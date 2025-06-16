class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def getNome(self):
        return self.__nome

    def getIdade(self):
        return self.__idade

    def getAltura(self):
        return self.__altura
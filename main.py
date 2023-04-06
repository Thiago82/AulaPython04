'''
class Cachorro:

    def __init__(self, nomecachorro, idadecachorro):
        self.nome = nomecachorro
        self.idade = idadecachorro

    def pega_nome(self):
          return self.nome

    def pega_idade(self):
          return self.idade

    def define_idade(self, idadecachorro):
        self.idade = idadecachorro


cachorro1_nome = "Popo"
cachorro1_idade = 2


    def rabo(self):
        print("Abana o rabo")

    def latir(self):
        print("Woof! Woof!")

    def lingua(self):
        return "Lambe"

    def pulgas(self, p):
        return p + 1

c = Cachorro("Lupi", 13)
c.define_idade(20)
print(c.pega_nome())

c2 = Cachorro("Saquinho", 5)
print(c2.pega_nome())

c.rabo()
c.latir()
c.lingua()
print(c.pulgas(9))
print(type(c))

class gato:

    def miar(self):
        print("Miauuu...")

g = gato()
g.miar()
print(type(g))'''  # CLASSES

'''
class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota  # 0 - 100

    def mostra_nota(self):
        return self.nota

class Curso:
    def __init__(self, nome, max_estudantes):
        self.nome = nome
        self.max_estudantes = max_estudantes
        self.estudantes = []

    def add_estudante(self, estudante):
        if len(self.estudantes) < self.max_estudantes:
            self.estudantes.append(estudante)
            return True
        return False

    def nota_media(self):
        valor = 0
        for estudante in self.estudantes:
            valor += estudante.mostra_nota()

        return valor / len(self.estudantes)

s1 = Estudante("Tim", 19, 85)
s2 = Estudante("Zezé", 21, 69)
s3 = Estudante("Estanislau", 18, 60)

curso = Curso("Ciência", 2)
curso.add_estudante(s1)
curso.add_estudante(s2)
print(curso.add_estudante(s3))  # Apenas print

print(curso.nota_media())'''  # MULTIPLAS CLASSES

'''
class Animal:  # Generalização
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def show(self):
        print(f"O animal {self.nome} possue {self.idade} anos de idade")

    def fala(self):
        print("Ele não sabe o que dizer")


class Gato(Animal):  # Invoca classe animal aqui
    def __init__(self, nome, idade, cor):
        super().__init__(nome, idade)  ## superclass, pega referencia da classe animal, e adiciona mais
        self.cor = cor

    def show(self):
        print(f"Eu sou o gato {self.nome}, possuo {self.idade} anos e sou {self.cor}")

    def fala(self):
        print("Eu faço Miau")


class Cachorro(Animal):  # Invoca classe animal aqui
    def fala(self):
        print("Ele faz Au-Au")

# Assim se trabalha a classe Animal
a = Animal("Blobo", 35)
a.show() # mostra a frase OU:
a.fala()

# Assim se invoca a classe Gato
g = Gato("Fred", 12, "cinza claro")
g.show()  #show e self da classe gato
g.fala()

# Assim se invoca a classe Cachorro
c = Cachorro("Cacau", 7)
c.show()  #show e self da classe gato
c.fala()'''  # HERANÇA DE CLASSES

'''
class Pessoa:
    numero_de_pessoas = 0

    def __init__(self, nome):
        self.nome = nome
        Pessoa.add_pessoa()


    @classmethod  ## "Decorator" denota que esta é uma classe método
    def numero_total(cls):
        return cls.numero_de_pessoas

    @classmethod
    def add_pessoa(cls):
        cls.numero_de_pessoas += 1


p1 = Pessoa("Jill")
p2 = Pessoa("Chris")
print(Pessoa.numero_total())'''  # ATRIBUTOS / CLASSES MÈTODO

'''
class Form:
    @staticmethod  ## Não pode ser acessada para alterar nada
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def rmv3(x):
        return x - 3

    @staticmethod
    def pr():
        print("Não precisa criar variável")

#Abaixo, não precisa invocar/indicar nada, apenas
# PRINT diretamente na classe staticmethod:
print(Form.add5(5))
print(Form.add10(5))
print(Form.rmv3(5))
Form.pr()'''  # STATIC METHODS






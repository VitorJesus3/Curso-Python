#Vamos começar criando um classe chamada carro
#Uma classe é um molde ou planta que define como os objetos dessa classe serão
# Ela define o que um objeto pode fazer (os metodos) e o que eles tem (os atributos)
class carro:
    # a classe carro tem dois atributos: "marca" e "modelo". E um método: acelerar.
    # um metodo especial __init__ é o que chama um objeto da classe
    # ele inicializa os atributos do objeto (marca e modelo)
    def __init__(self, marca, modelo,cor):
      # os atributos do objeto serão definidos dentro init
      # o self refere-se ao propio objeto que está sendo criado
      self.modelo = modelo  #atributo que armazena o modelo
      self.marca = marca    #atributo que armazena a marca
      self.cor = cor

    # Esse é o metodo que define o comportamento do objeto, aqui estamos falndo o que de fato o carro faz
    def acelerar(self):
      print(f'O {self.marca} {self.modelo} esta acelerando. ')
    
    def parar(self):
      print(f'O {self.marca} {self.modelo} parou! ')

    def direita(self):
      (f" O {self.marca}{self.modelo}{self.cor} virou a direita!")

    def esquerda(self):
      (f" O {self.marca}{self.modelo}{self.cor} virou a esquerda!")

carro1 = carro("Fusca", " 1984", " Preto")
print(carro1.marca)
print(carro1.modelo)
print(carro1.cor)
carro1.acelerar()
carro1.direita()
carro1.esquerda()
carro1.parar()

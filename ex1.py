# exercicio 1

# criando classe
class Produto:
    def __init__(self, codigo, nome, precoUni):
        self.codigo = codigo
        self.nome = nome
        self.precoUni = precoUni
    def mostrar(self):
        print(f"Nome: {self.nome}\nPreco unitário: {self.precoUni}\nCógido do produto: {self.codigo}\n")
        
# criando objetos
produto1 = Produto(7828778382, "Estojo", 11.99)
produto2 = Produto(7997238245, "Porta", 499.94)
produto1.mostrar()
produto2.mostrar()
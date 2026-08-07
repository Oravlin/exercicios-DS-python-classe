class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar(self):
        print(f"Produto: {self.nome}|Preço:{self.preco}")
        
# criando objeto
p1 = Produto("Mouse", 50)
p2 = Produto("Teclado", 70)
p1.mostrar()
p2.mostrar()
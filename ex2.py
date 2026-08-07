# criando lista dos produtos:
listProd = []

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar():
        print(f"Produto: {self.nome}|Preço: {self.preco}")
        
def cadProd():
    nomeProd = input("Insira o nome do produto: ")
    while True:
        try:
            precoProd = float(input("Insira o preco do produto: "))
            if (precoProd <= 0):
                print("Insira um valor maior que 0!")
                continue
            break
        except ValueError:
            print("Valor inválido! Insira apenas valores numéricos")
    produtoCadastro = Produto(nomeProd, precoProd)
    listProd.append(produtoCadastro)
    
def listarProds():
    for produto in listProd:
        print(f"Índice: {listProd.index(produto)}\nProduto: {produto.nome}\nPreço: {produto.preco}")
        
def comprarProd():
    while True:
        try:
            p = listProd[input("Insira o índice do produto: ")]
            break
        except IndexError:
            print("Índice inválido! Insira um índice que exista! (lembre-se: o índice sempre começa pelo 0!)")
    while True:
        try:
            qtd = int(input("Insira a quantidade que deseja pagar: "))
            break
        except ValueError:
            print("Valor inválido! Digite um valor inteiro")
    pPreco = p.preco
    if 
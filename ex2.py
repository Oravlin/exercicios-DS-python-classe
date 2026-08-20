# criando lista dos produtos:
listProd = []

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def mostrar(self):
        print(f"Produto: {self.nome}\nPreço: {self.preco}\n")
        
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
    print(f"Produto cadastrado!")
    
def listarProds():
    for produto in listProd:
        print(f"Índice: {listProd.index(produto)}")
        produto.mostrar()
        
def comprarProd():
    while True:
        try:
            #pega o produto já cadastrado
            p = listProd[int(input("Insira o índice do produto: "))]
            break
        except IndexError:
            print("Índice inválido! Insira um índice que exista! (lembre-se: o índice sempre começa pelo 0!)")
        except ValueError:
            print("Valor inválido! Insira um valor numérico válido!")
    #exibe o produto selecionado
    print(f"Produto selecionado: {p.nome} Preço: {p.preco}")
    while True:
        try:
            qtd = int(input("Insira a quantidade que deseja pagar: "))
            break
        except ValueError:
            print("Valor inválido! Digite um valor inteiro")
    pPreco = p.preco
    valorTotal = pPreco * qtd
    print(f"O valor total a pagar será: {valorTotal}")
    if valorTotal >= 100:
        print("Desconto disponível!\n")
    else:
        print("Desconto indisponível!\n")
#loop principal
while True:
    escolha = input("O que deseja fazer?\n[1] para cadastrar produtos|[2] para comprar produtos|[3] para listar produtos|[4] para encerrar programa: ")
    if escolha == "1":
        cadProd()
    elif escolha == "2":
        comprarProd()
    elif escolha == "3":
        listarProds()
    elif escolha == "4":
        print("\nEncerrando programa...\n")
        break
    else:
        print("Digite uma das opções válidas\n")
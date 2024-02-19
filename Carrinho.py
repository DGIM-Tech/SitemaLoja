class Carro:
    def __init__(self):
        self.carrinho = []
    

    def AdcionarProdutos(self , produto):
        self.carrinho.append(produto)
        print(f"Produto '{produto}' acinado ao carrinho")


    def RelizarComprar(self, codico):
        for produto in self.carrinho:
            if produto.codico == codico:
                print(f"Compra Realizada com sucesso '{produto.nome}' ")
                self.carrinho.remove(produto)
                return
        print(f"Produto como coidoc {codico} nao encontrado no carrinho")

    def DeletarProduto(self, codico):
        for produto in self.carrinho:
            if produto.codico == codico:
                self.carrinho.remove(produto)
                print(f"produto com o codico {codico} removido do carrinho")
                return
        print(f"Produto com o codico {codico} Nao encontrado")

    def calcularValorTotal(self):
        total = sum(produto.preco for produto in self.carrinho)
        return total
    
    def ExibirProdutos(self):
        if not self.carrinho:
            print("o carrinho esta vazio por favor adcione novos produtos")

        else: 
            print("Produtos do carrinho: ")
            for produto in self.carrinho:
                print(produto)
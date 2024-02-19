from Produto import Produto

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def AdcionarProduto(self, produto):
        self.produtos.append(produto)
        print(f"Produto {produto.nome} adcionado á categoria {self.nome}")

    def removerProduto(self, produto):
        if produto in self.produtos:
            self.produtos.remove(produto)
            print(f"Produto {produto.nome} removido da categoria {self.nome} com sucesso")
        else:
            print(f"Produto {produto.nome} nao encontrado na categoria")


    def ListaProduto(self):
        print(f"produtos na categoria {self.nome}")
        for produto in self.produtos:
            print(f"{produto.nome} - R$ {produto.preco} - {produto.discricao} - {produto.garantia}")

    def AtualizarCategroia(self, novo_categoria):
        self.nome = novo_categoria
        print(f"categoria Atualizad: {self.nome}")

    def RemoverCategoria(self, nome):
        if self.nome == nome:
            for produto in self.produtos:
                produto.remover_da_categoria()
            self.produtos.clear()

            del self
            print(f"categroia {nome} removida")
        else:
            print(f"categroia {nome} nao encontrada")

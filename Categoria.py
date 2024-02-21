from Produto import Produto

class Categoria:
    def __init__(self, nome, gerenteLogado=None):
        self.nome = nome
        self.produtos = []
        self.gerenteLogado = gerenteLogado

    def AdcionarProduto(self, produto):
        if self.gerenteLogado:
            self.produtos.append(produto)
            print(f"Produto {produto.nome} adcionado á categoria {self.nome}")
        else:
            print("Apenas o gerente logado pode adcionar produtos")
    def removerProduto(self, produto):
        if self.gerenteLogado:
            if produto in self.produtos:
                self.produtos.remove(produto)
                print(f"Produto {produto.nome} removido da categoria {self.nome} com sucesso")
            else:
                print(f"Produto {produto.nome} nao encontrado na categoria")
        else:
            print("Apenas o gerente logado pode remover produtos")

    def ListaProduto(self):
        print(f"produtos na categoria {self.nome}")
        for produto in self.produtos:
            print(f"{produto.nome} - R$ {produto.preco} - {produto.discricao} - {produto.garantia}")

    def AtualizarCategroia(self, novo_categoria):
        if self.gerenteLogado:
            self.nome = novo_categoria
            print(f"categoria Atualizad: {self.nome}")
        else:
            print("Apenas o gerente logado pode editar categorias")
    def RemoverCategoria(self, nome):
        if self.gerenteLogado:
            if self.nome == nome:
                for produto in self.produtos:
                    produto.remover_da_categoria()
                self.produtos.clear()

                del self
                print(f"categroia {nome} removida")
            else:
                print(f"categroia {nome} nao encontrada")
        else:
            print("Apenas o gerente logado pode remover produtos da categoria")
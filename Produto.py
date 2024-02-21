
class Produto:
    def __init__(self, codico, nome, preco, discricao, garantia,  categoria = None, gerenteLogado=None ):
        self.codico = codico
        self.nome = nome
        self.preco = float(preco)
        self.discricao = discricao
        self.garantia = garantia
        self.gerenteLogado = gerenteLogado
        self.categoria = categoria
        if categoria:
            categoria.AdcionarProduto(self)
    def __str__(self):
        return f"Produto: {self.nome}, (Código: {self.codico}, Preço: R${float(self.preco):.2f}, Descricao: {self.discricao}, garantia: {self.garantia})"

    def AtualizarProdutos(self, novo_preco):
        if self.gerenteLogado:
            self.preco = novo_preco
            print(f"Produto atulizado: R$ {self.preco}")
        else:
            print("Apenas o genre logado pode atualizar produtos")
    def remover_da_categoria(self):
        if self.gerenteLogado:
            if self.categoria:
                self.categoria.remover_produto(self)
                self.categoria = None
                print(f"Produto {self.nome} removido da categoria.")
        else:
            print("Apenas o genre logado pode remover produtos")
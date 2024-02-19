from Usuario import Usuario
from Cliente import Cliente
from Gerente import Gerente
from Categoria import Categoria
from Produto import Produto
from Carrinho import Carro
from GereciaLoja import *
menu()

c = Cliente("Maria", "123", "mariana",  "1")

g = Gerente("gerson", '123' , "gerson Breno", "2")
g.Login("gerson", "123")


c1 = Categoria("eletronicos")
c2 = Categoria("teste")

p1 = Produto(1, "celiular", "980", "celular simples", "garintia de um ano", c1, g)
p2 = Produto("2", "noor", "980", "celular simples", "garintia de um ano", c1, g)
c1.AdcionarProduto(p1)
c.adcionarProdutos(p1)
c.adcionarProdutos(p2)

# p1.AtualizarProdutos("celular", "1000")
# c.carro.RelizarComprar(1)

c.carro.ExibirProdutos()
# c.carro.RelizarComprar("2")
# 
# total = c.carro.calcularValorTotal()
# print(f"total {total}")








# c2.RemoverCategoria("t")
# c1.RemoverCategoria("eletronicos")
# c1.ListaProduto()
# c2.ListaProduto()



# c.CadastrarCliente(c)
# c.Login("Maria","123")
# print("--------------------------")
# g.CadastrarGerente(g)

# g.Login("gerson", "123")

# usuario = input("informe o usuario")
# senha = input("informe a senha: ")
# nome = input("informe o nome")
# enderco = input("informe o enderco")
# c = Cliente(usuario, senha, nome, enderco)

# print('exibir informaçao \n')
# c.Exibir_informacao()
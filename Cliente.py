from Usuario import Usuario
from Carrinho import Carro

class Cliente(Usuario):
    def __init__(self, usuario, senha, nome, cpf):
        super().__init__(usuario, senha, nome, cpf)
        self.carro = Carro()
        self.listaCliente = []

    def adcionarProdutos(self, produto):
        self.carro.AdcionarProdutos(produto)

    def CadastrarCliente(self, novoCliente):
        self.listaCliente.append(novoCliente)
        print(f"Usuario {novoCliente.nome} cadastrado com sucesso")

    def Login(self, usuario, senha):
        for cliente in self.listaCliente:
            if cliente.usuario == usuario and cliente.senha == senha:
                print(f"Login Realizado com sucesso. Bem vindo. {cliente.nome}!")
                return True
        print("Falha a realizar o Login, Usuario e/ou Senha invalido. Tente novamente.")
        return False


        

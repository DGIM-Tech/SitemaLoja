from Gerente import Gerente
from Cliente import Cliente
class GereciaLoja:
    def __init__(self) -> None:
        self.listaGerentes = []
        self.listaClientes = []
    def CadastrarGerente(self, usuario, nome, senha, cpf):
        novo_gerente = Gerente(usuario, nome, senha, cpf)
        self.listaGerentes.append(novo_gerente)
        print(f"Gerente {novo_gerente.nome} cadastrado com sucesso")

    def Login(self, usuario, senha):
        for gerente in self.listaGerentes:
            if gerente.usuario == usuario and gerente.senha == senha:
                print(f"Login realizado com sucesso. Seja bem-vindo, {gerente.nome}!")
                return gerente

        print("Usuário ou senha incorretos. Tente novamente.")
        return None
    
    def CadastrarCliente(self,usuario, nome, senha, cpf ):
        novo_cliente = Cliente(usuario, nome, senha, cpf)
        print(f"Usuario {novo_cliente.nome} cadastrado com sucesso")

    def Login(self, usuario, senha):
        for cliente in self.listaCliente:
            if cliente.usuario == usuario and cliente.senha == senha:
                print(f"Login Realizado com sucesso. Bem vindo. {cliente.nome}!")
                return True
        print("Falha a realizar o Login, Usuario e/ou Senha invalido. Tente novamente.")
        return False



    def menu(self):
        print("Bem-vindo à Loja!")
        print("1. Área do Gerente ")
        print("2. Área do Cliente")
        print("3. Sair")

    def menu_cliente(self):
        print("\nÁrea do Cliente:")
        print("1. Realizar cadastro")
        print("2. ralizar login")
        print("3. Lista dos produtos")
        print("4. volta menu anterio")

    def menu_gerente(self):
        print("\nÁrea do Gerente:")
        print("1. realizar cadastro")
        print("2. reazlizar login")
        print("3 volta menu anterio")
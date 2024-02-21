from Usuario import Usuario

class Gerente(Usuario):
    def __init__(self, usuario = None, nome = None, senha = None, cpf = None):
        super().__init__(usuario, nome, senha, cpf)
       
        self.cpf = cpf
        
        



    # def Login(self, usuario, senha):
    #     for gerente in self.listaGerentes:
    #         if gerente.usuario == usuario and gerente.senha == senha:
    #             print(f"Login reliaza com sucesso. Seja bem, {gerente.nome}!")
    #             return gerente
    #     print("senha e usuario incorreto tente novamente")
    #     return False

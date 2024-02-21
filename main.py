from Usuario import Usuario
from Cliente import Cliente
from Gerente import Gerente
from Categoria import Categoria
from Produto import Produto
from Carrinho import Carro
from GereciaLoja import *


from GereciaLoja import GereciaLoja
from Gerente import Gerente

gl = GereciaLoja()
gerentes = Gerente()  # Cria uma instância fora do loop

while True:
    gl.menu()
    op = input("Escolha uma opção acima: ")

    if op == '1':
        while True:
            gl.menu_gerente()
            op_gerente = input("Escolha uma opção acima: ")

            if op_gerente == '1':
                nome = input("Digite o seu nome: ")
                cpf = input("Digite o seu cpf: ")
                usuario = input("Crie o seu nome de usuário: ")
                senha = input("Crie a sua senha: ")
               
                gl.CadastrarGerente(usuario, nome, senha, cpf)

            elif op_gerente == '2':
                usuario1 = input("Digite seu nome de usuário: ")
                senha1 = input("Digite sua senha: ")
                gl.Login(usuario1, senha1)

            elif op_gerente == '3':
                break

    elif op == '2':
        while True:
            gl.menu_cliente()
            op_cliente = input("Escolha uma opção acima: ")
            if op_cliente == '1':
                nome = input("Digite o seu nome: ")
                cpf = input("Digite o seu cpf: ")
                usuario = input("Crie o seu nome de usuário: ")
                senha = input("Crie a sua senha: ")
                gl.CadastrarCliente(usuario, nome, senha, cpf)

            elif op_cliente == '4':
                break


    elif op == '3':
        print("Saindo do sistema.....")
        break  # Saia do loop principal

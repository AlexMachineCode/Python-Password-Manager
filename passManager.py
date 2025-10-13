import random
import string
from cryptography.fernet import Fernet
import os
from tabulate import tabulate


def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)


def carregar_chave():
    return open("chave.key", "rb").read()


if not os.path.exists("chave.key"):
    gerar_chave()


chave = carregar_chave()
cipher_suite = Fernet(chave)


def adicionar_senha():
    site = input("Digite o nome do site: ")
    senha = input("Digite a senha: ")
    senha_criptografada = cipher_suite.encrypt(senha.encode())
    
    with open("senhas.txt", "a") as arquivo:
        arquivo.write(f"{site} | {senha_criptografada.decode()}\n")
    
    print("Senha para {} adicionada com sucesso!".format(site))



def visualizar_senhas():
    if not os.path.exists("senhas.txt"):
        print("Não há senhas salvas.")
        return

    senhas = []
    
    with open("senhas.txt", "r") as arquivo:
        for linha in arquivo.readlines():
            site, senha_criptografada = linha.strip().split(" | ")
            senha = cipher_suite.decrypt(senha_criptografada.encode()).decode()
            senhas.append([site, senha])

    
    print(tabulate(senhas, headers=["Site", "Senha"], tablefmt="grid"))


def remover_senha():
    site = input("Digite o nome do site para remover a senha: ")
    linhas = []
    encontrado = False

    if not os.path.exists("senhas.txt"):
        print("Não há senhas salvas.")
        return

   
    with open("senhas.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    
    with open("senhas.txt", "w") as arquivo:
        for linha in linhas:
            if not linha.startswith(site):
                arquivo.write(linha)
            else:
                encontrado = True

    if encontrado:
        print(f"Senha para {site} removida com sucesso!")
    else:
        print(f"Não foi encontrada uma senha para {site}.")


def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(comprimento))
    return senha


def menu():
    while True:
        print("\nGerenciador de Senhas")
        print("1. Adicionar Senha")
        print("2. Visualizar Senhas")
        print("3. Remover Senha")
        print("4. Gerar Senha Aleatória")
        print("5. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar_senha()
            visualizar_senhas()
        elif escolha == '2':
            visualizar_senhas()
        elif escolha == '3':
            remover_senha()
            visualizar_senhas()
        elif escolha == '4':
            comprimento = int(input("Digite o comprimento da senha (padrão 12): ") or 12)
            senha_gerada = gerar_senha(comprimento)
            print(f"Sua senha gerada é: {senha_gerada}")
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()

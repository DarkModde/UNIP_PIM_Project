import json
import os

# Função para salvar os usuários no arquivo JSON
def salvar_usuarios(usuarios):

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo)

# Função para carregar os usuários do arquivo JSON
def carregar_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}  # Retorna um dicionário vazio se o arquivo não existir

# Função para cadastrar um novo usuário
def cadastrar():
    usuarios = carregar_usuarios()

    os.system('cls')
    print("\n=== Cadastro de Usuário ===")
    nome = input("Digite um nome de usuário: ")

    if nome in usuarios:
        print("Usuário já existe!")
        return menu()

    senha = input("Digite uma senha: ")
    usuarios[nome] = senha

    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")
    return menu()

# Função para fazer login
def login():
    os.system("cls")
    usuarios = carregar_usuarios()

    print("\n=== Login ===")
    nome = input("Digite seu nome de usuário: ")
    senha = input("Digite sua senha: ")

    if nome in usuarios and usuarios[nome] == senha:
        os.system('cls')
        print("Login bem-sucedido!")
    else:
        os.system('cls')
        print("Usuário ou senha incorretos.")
        return menu()

# Menu principal do sistema
def menu():
    print("\n=== Sistema de Login ===")
    print("1 - Login")
    print("2 - Cadastrar")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        login()
    elif escolha == "2":
        cadastrar()
    else:
        print("Opção inválida!")

os.system('cls')
menu()

# Arte ASCII

print("============================================================================================")
print(r"""
  ____                                           __                                          
 /\  _`\                                        /\ \                                         
 \ \,\L\_\    _____      __       ___      __   \ \ \         __      __      _ __    ___    
  \/_\__ \   /\ '__`\  /'__`\    /'___\  /'__`\  \ \ \  __  /'__`\  /'__`\   /\`'__\/' _ `\  
    /\ \L\ \ \ \ \L\ \/\ \L\.\_ /\ \__/ /\  __/   \ \ \L\ \/\  __/ /\ \L\.\_ \ \ \/ /\ \/\ \ 
    \ `\____\ \ \ ,__/\ \__/.\_\\ \____\\ \____\   \ \____/\ \____\\ \__/.\_\ \ \_\ \ \_\ \_\
     \/_____/  \ \ \/  \/__/\/_/ \/____/ \/____/    \/___/  \/____/ \/__/\/_/  \/_/  \/_/\/_/
                \ \_\                                                                        
                 \/_/                                                                        

""")
print('============================================================================================')

# Exibir a arte no terminal


# Função que explica o Pensamento Lógico Computacional
def pensamento_logico():
    os.system('cls')
    print('> Pensamento Lógico Computacional:')
    print("-------------------------------------------------------")
    print('1. Algoritmos e Fluxogramas: São sequências de instruções que visam resolver problemas de maneira lógica e estruturada. '
          'Os algoritmos ajudam no planejamento e organização da solução, enquanto os fluxogramas representam graficamente o fluxo de execução, facilitando o entendimento e a implementação.')
    print("-------------------------------------------------------")

def estruturas_de_controle():
    os.system('cls')
    print('> Estruturas de Controle:')
    print("----------------------------------------------")
    print('2. Estruturas de controle são comandos e instruções que determinam a ordem de execução dos blocos de código em um programa. '
          'Essas estruturas permitem tomar decisões, repetir ações e alterar o fluxo do programa, sendo essenciais para a criação de algoritmos que respondem a diferentes condições e variáveis.')
    print("----------------------------------------------")

def desempenho_e_complexidade():
    os.system('cls')
    print('> Desempenho e Complexidade:')
    print("------------------------------------------------")
    print('3. A análise de desempenho e complexidade tem como objetivo avaliar a eficiência de algoritmos, sistemas e processos computacionais. '
          'Essa avaliação é realizada com base no tempo e no espaço necessários para executar o algoritmo, considerando diferentes tamanhos de entrada, e ajuda a identificar soluções mais eficientes.')
    print("------------------------------------------------")

def decomposicao_e_abstracao():
    os.system('cls')
    print('> Decomposição e Abstração:')
    print("-----------------------------------------------")
    print('4. Decomposição é o processo de dividir um problema complexo em partes menores e mais simples, facilitando a organização do código e a solução das etapas. '
          'Já a abstração consiste em esconder os detalhes complexos e focar apenas no essencial, o que torna o código mais legível, reutilizável e fácil de manter.')
    print("-----------------------------------------------")
# Função para o menu


def menu():
    while True:
        # Exibindo as opções de menu
        print(" ")
        print("1. Pensamento Lógico Computacional")
        print('2. Estruturas de controle')
        print('3. Desempenho e Complexidade')
        print('4. Decomposição e abstração')
        print("0. Sair")
        print(" ")

        try:
            # Solicita ao usuário que digite sua escolha
            escolha = int(input("Digite a opção desejada: "))

            # Verifica a escolha do usuário
            if escolha == 1:
                pensamento_logico()  # Chama a função de pensamento lógico
            elif escolha == 2:
                estruturas_de_controle()
            elif escolha == 3:
                desempenho_e_complexidade()
            elif escolha == 4:
                decomposicao_e_abstracao()
            elif escolha == 0:
                print("Saindo do programa...")
                break  # Encerra o loop e sai do programa
            else:
                print("Opção inválida, por favor, escolha novamente.")

        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")


# Inicia o menu
menu()

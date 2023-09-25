"""
Agenda de contatos:
- desenvolvimento de uma agenda de contatos persistindo as informações em arquivo.
Especificidades do programa:
1 - Criação de um arquivo agenda com os três métodos.
    a. Adição de contato.
    b. Listagem de contatos.
    c. Remoção de contatos.
2 - Criação de um arquivo principal para a aplicação que importar o módulo de agenda 
e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.
"""
import os

def add_contato():
    nome = input("informe o nome.\n")
    endereco = input("informe o endereço.\n")
    telefone = input("informe o telefone.\n")

    contato = f"Nome: {nome} \nEndereço: {endereco} \nTelefone: {telefone}\n"

    with open("Arquivos/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contato)

def ver_contatos():
    if not os.path.exists("Arquivos/contatos.txt"):
        print("Lista de contatos vazia.")
        return
    with open("Arquivos/contatos.txt", "r", encoding="utf-8") as file:
        contatos = file.read()
    print("Lista de contatos.")
    print(contatos)

def del_contatos():
    if not os.path.exists("Arquivos/contatos.txt"):
        print("Lista de contatos vazia.")
        return
    with open("Arquivos/contatos.txt", "w", encoding="utf-8") as file:
        file.write("")

print("contato excluido com sucesso")
from exercicio_agenda_de_contatos import add_contato, ver_contatos, del_contatos

def main():
    while True:
        print("\nAgenda de contatos.")
        print("1. Adicionar contato.")
        print("2. Ver contatos da agenda.")
        print("3. Deletar contato.")
        print("4. Sair.")

        escolha = input("Escolha a opção de 1 a 4.\n")
        if escolha == "1":
            add_contato()
        elif escolha == "2":
            ver_contatos()
        elif escolha == "3":
            del_contatos()
        elif escolha == "4":
            break
        else:
            print("Escolha uma opção valida.")
    
main()       
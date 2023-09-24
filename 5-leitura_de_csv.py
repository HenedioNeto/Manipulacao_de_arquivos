# Leitura de um arquivo csv

with open("Arquivos/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linhas = line.rstrip().split(",") # Traz os dados em forma de lista
        print(linhas[0]) # Traz apenas os dados no indice 0 (no caso os cursos)
        linguagem, categoria = line.rstrip().split(",")
        print(f"{linguagem}-{categoria}")
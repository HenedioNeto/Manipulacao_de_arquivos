# Criando um dicionario com as informações do arquivo csv a partir do arquivo csv

cursos = []

with open("Arquivos/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.strip().split(",")
        curso = {}
        curso["linguagem"] = linguagem
        curso["categoria"] = categoria
        cursos.append(curso)
print(cursos)

for curso in cursos:
    print(f"{curso['linguagem']} -{curso['categoria']}")
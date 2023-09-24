# Ordenação de lista em arquivo csv (decrescente com reverse=True)

cursos = []

with open("Arquivos/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.strip().split(",")
        cursos.append(f"{linguagem}-{categoria}")

for curso in sorted(cursos, reverse=True):
        print(curso)
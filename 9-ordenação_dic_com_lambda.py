# Ordenando valores em dicionarios usando funções lambda

cursos = []

with open("Arquivos/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.strip().split(",")
        curso = {}
        curso["linguagem"] = linguagem
        curso["categoria"] = categoria
        cursos.append(curso)
print(cursos)

# Ordenação usando lambda
for curso in sorted(cursos, key=lambda curso: curso["categoria"]):
    print(f"{curso['linguagem']} -{curso['categoria']}")
# Leitura de csv em dicionario usando modulo builtin
import csv

cursos = []

with open("Arquivos/cursos.csv", "r", encoding="utf-8") as file:
    leitura = csv.DictReader(file)
    for linha in leitura:
        cursos.append({"linguagem":linha["linguagem"], "categoria":linha["categoria"]})
print(cursos)

for curso in sorted(cursos, key=lambda curso: curso['linguagem']):
    print(f"{curso['linguagem']} -{curso['categoria']}")

# Ao reconhecer o arquivo como dicionario ele tira as informações linguagem e categoria
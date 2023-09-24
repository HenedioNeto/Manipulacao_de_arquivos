# Ordenando valores em dicionarios (reverse=True inverte a ordenação)

cursos = []

with open("Arquivos/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.strip().split(",")
        curso = {}
        curso["linguagem"] = linguagem
        curso["categoria"] = categoria
        cursos.append(curso)
print(cursos)

# Função que define a chave que será usada para fazer a ordenação
def get_linguagem(curso):
    return curso["linguagem"]

def get_categoria(curso):
    return curso["categoria"]

for curso in sorted(cursos, key=get_categoria):
    print(f"{curso['linguagem']} -{curso['categoria']}")
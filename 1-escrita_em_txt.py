# Criação de um arquivo txt e adição do conteúdo

name = input('Digite seu nome:\n')
"""
- Arquivos:
1 - opção w - write
2 - opção a - append
3 - opção r - read
"""

# Alternativa 1
file = open("Arquivos/names.txt", "a", encoding="utf-8")
file.write(f"{name.rstrip()}\n")
file.close()

# Alternativa 2
with open("Arquivos/names.txt", "a", encoding="utf-8") as file:
    file.write(f"{name.rstrip()}\n")
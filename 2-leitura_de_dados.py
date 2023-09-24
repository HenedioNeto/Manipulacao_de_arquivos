# Leitura do arquivo criado

"""
- Arquivos:
1 - opção w - write
2 - opção a - append
3 - opção r - read
"""

with open("Arquivos/names.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(f"Retorno do conteúdo sem espaço: {line.rstrip()}")
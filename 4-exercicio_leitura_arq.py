"""
Lendo n linhas de um arquivo
- escrever um programa que leia as primeiras n linhas de um arquivo.
1 - O nome do arquivo e a quantidade de linhas devem ser passadas 
via parametro da função

opção r - read

"""
from itertools import islice

name_arq = input('Qual será o arquivo lido?:\n')
linhas = int(input('Quantas linhas deseja ler do arquivo?:\n'))

def leitura_arq(name_arq, qtd_linhas):
    with open(name_arq, "r", encoding="utf-8") as file:
        for line in islice(file, qtd_linhas):
            print(line.rstrip())

print(leitura_arq(name_arq, linhas))
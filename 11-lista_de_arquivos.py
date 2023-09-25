# os modulos... glob da acesso as informações de arquivos em diretorios, os pe modulo para sistema operacional e zipfile compacta arquivos
import glob, os, zipfile

# 1 - Diretório de trabalho atual
os.getcwd()

# 2 - Listar todos arquivos txt (os asterisco permite pegar mais de 1 arquivo txt)
for file in glob.glob("Arquivos/*.txt"):
    print(file)

# 3 - Listar todos arquivos csv
for file in glob.glob("Arquivos/*.csv"):
    print(file)

# 4 - Compactar arquivos txt
with zipfile.ZipFile('txt.zip', 'w') as zip:
    for file in glob.glob("Arquivos/*.txt"):
        zip.write(file)

# 5 - Compactando arquivos csv
with zipfile.ZipFile('csv.zip', 'w') as zip:
    for file in glob.glob("Arquivos/*.csv"):
        zip.write(file)

# 6 - Compactar todos os arquivos
with zipfile.ZipFile('codigos.zip', 'w') as zip:
    for file in glob.glob("*"):
        zip.write(file)
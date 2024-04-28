with open('adult.data', 'r') as file:
    # Ler todas as linhas do arquivo
    lines = file.readlines()

# Abrir o arquivo para escrita
with open('adult.data', 'w') as file:
    # Escrever as linhas modificadas no arquivo
    for line in lines:
        # Remover os espaços em branco de cada linha e escrever a linha modificada no arquivo
        file.write(line.replace(' ', ''))
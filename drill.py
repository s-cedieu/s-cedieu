file_name = input("¿Cuál es el nombre del archivo? ")

with open(file_name, 'w') as f:
    line1 = input("line 1: ")
    f.write(line1 + '\n')
    print("Ve a mirar el archivo txt.")
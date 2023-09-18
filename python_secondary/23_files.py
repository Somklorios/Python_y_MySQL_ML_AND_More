file = open("./text.txt")

#print(file.read()) # <---- esta linea, nos permite leer #TODO# el archivo que enlazamos 

#print(file.readline()) # <--- Esto nos permite leer solo UNA del archivo enlazado, ya es que muy liviano 

#print(file.readline())
#print(file.readline())
#print(file.readline())

for line in file:
    print(line)

file.close()

with open('./text.txt') as file:
    for line in file:
            print(line)
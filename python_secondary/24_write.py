with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('nuevas cosas en este archivo\n')
    file.write('hola archivo\n') 
    file.write('nmas lineas\n')           


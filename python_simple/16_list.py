#listas siempre con []
#Puede ser modificada
#Cada elemento esta separado por una coma
#Puede contener todo tipo de datos

numbers = [1, 2, 3, 4, 5, 6, 7]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

#puedo agregar varios datos a una lista
types = [1, True, 'hola']
print(types)

print(numbers[0])
print(tasks[0])
text = 'Hola'
# text[0] = 'W'

tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('hola' in types)

#los strings no se pueden alterar, las listas si
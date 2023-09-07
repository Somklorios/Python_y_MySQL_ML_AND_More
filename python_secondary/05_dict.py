dict = {}
for i in range(1, 11):
    dict[i] = i * 2
print(dict)    


dict_v2 = {i : i * 2 for i in range(1, 5)}
print(dict_v2)


import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)

print(population)
print("*" * 20 )
#                  #llave   #valor                 #iteracion
population_v2 = { country: random.randint(1, 100) for country in countries}
print(population_v2)

names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

print(list(zip(names, ages)))
# zip es una funcion que une dos listas
# con list ya podemos transforma las cosas en listas

new_dict = {name: age for (name, age) in zip(names,ages)}
print(new_dict)

# creamos un par clave/valor al diccionario
# el (name, age)viene de iterar una lista con tuplas
# ese merge lo obtenemos de la union de las listas de name y ages
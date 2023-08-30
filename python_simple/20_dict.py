person = {
  'name': 'nico',
  'last_name': 'molina',
  'langs': ['python', 'javascript'],
  'age': 99
}

print(person)

person['name'] = 'santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

#usamos del para eliminar el item que yo quiero
del person['last_name']
person.pop('age')

print(person)

#cuando llamamos al comando items, nos regresa todos los elemtoss en forma de lista
print('items')
print(person.items())


print('keys')
print(person.keys())

#cuando llamamos al comando values, nos regresa solo los valores
print('values')
print(person.values())

#entendí que al usar el keys() o values() ya te devolvía una lista con las llaves o los valores.
#¿Por qué hay que aplicar un list para pasarlo a lista nuevamente?

#La razón es que si solo se imprime lo que retorna la función keys() o values() esto nos devuelve una TUPLA y no será el mismo tipo de dato de retorno que pide el ejercicio en el punto 4 y 5, es decir una LISTA.
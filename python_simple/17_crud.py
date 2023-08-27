#CRUD, Create, Read, Update & Delete

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[1])

numbers[-1] = 10
print(numbers)

#append(): Añade un ítem al final de la lista.
numbers.append(700)
print(numbers)

#insert(): Agrega un ítem a la lista en un índice específico
numbers.insert(0, "hola")
print(numbers)

numbers.insert(3, "change")
print(numbers)

tasks = ["todo 1", "todo 2", "todo 3", "todo 4"]
new_list = numbers + tasks
print(new_list)

#index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
index =new_list.index("todo 2")
new_list[index] = "todo changed"
print(new_list)

#remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
new_list.remove('todo 1')
print(new_list)

#pop(): Extrae un ítem de la lista y lo borra.
new_list.pop()
print(new_list)

new_list.pop(0)
print(new_list)

#reverse(): Le da la vuelta a la lista actual.
new_list.reverse()
print(new_list)

#sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
numbers_a = [1, 4, 6 , 3]
numbers_a.sort()
print(numbers_a)

#sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor
strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)

new_list.sort()


#append(): Añade un ítem al final de la lista.
#insert(): Agrega un ítem a la lista en un índice específico
#clear(): Vacía todos los ítems de una lista.
#extend(): Une una lista a otra.
#count(): Cuenta el número de veces que aparece un ítem.
#index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
#pop(): Extrae un ítem de la lista y lo borra.
#remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
#reverse(): Le da la vuelta a la lista actual.
#sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.

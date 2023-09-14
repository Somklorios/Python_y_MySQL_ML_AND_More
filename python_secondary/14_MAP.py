#La función map () ejecuta una función especifica para cada elemento en un iterable y el elemento se envía a la función como un parámetro.

# Sintaxis.
#        map(function, iterables)

#Con esto utilizáremos maps()



numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
   numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)   
print(numbers_v2) 
print(numbers_v3)  


numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]


print(numbers_1) 
print(numbers_2) 
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))

print(result)

# tiene el limite de la lista mas pequeña, asi 4 no tendra con quien iterar
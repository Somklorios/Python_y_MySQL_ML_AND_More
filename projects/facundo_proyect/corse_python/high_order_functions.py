my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = [ i for i in my_list if i % 2 != 0]
# para todas las i dentro de mi lista voy a guardas a las i solamente si esas i %(modulo 2) son distintas de 0

print(odd)

#uso con filter

my_list2 = [1, 4, 5, 6, 9, 13, 19, 21]
odd_2 = list(filter(lambda x: x%2 != 0, my_list2))
print(odd_2)


print ("*" * 34)

#uso de MAP
my_list3 = [1, 2, 3, 4, 5]
squares = [i**2 for i in my_list3]
print(squares)

my_list3= [1, 2, 3, 4, 5]
odd_3 = list(map(lambda x: x**2, my_list3))
print(odd_3)


print ("*" * 34)


#uso de REDUCE

my_list4 = [ 2, 2, 2, 2, 2]
all_multiplied = 1

for i in my_list4:
    all_multiplied = all_multiplied * i 
print(all_multiplied)    

from functools import reduce
my_list4 = [ 2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, my_list4)

print(all_multiplied)
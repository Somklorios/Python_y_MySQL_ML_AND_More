# no tiene un par key-value, así me doy cuenta que es un set, un conjunto.
set_conuntries = {'col', 'mex', 'bol'}
print(set_conuntries)
print(type(set_conuntries))

# si yo pongo algo repetido, él me lo quita al imprimir
set_numbers = {1, 2, 4, 44, 555}
print(set_numbers)

# puede ser mixto. El set se ordena solo, lo importante es lo que tengo dentro.
set_types = {1, "dos", False, 12.12}
print(set_types)

# la podemos crear a partir de un string
set_from_string = set('hoola')
print (set_from_string)

# la podemos crear a partir de una tupla
set_from_tuples = set (('abc','cbv','as','abc'))
print (set_from_tuples)

# la podemos crear a partir de una lista
numbirs = [1,2,3,1,2,3,4]
set_numbirs= set(numbirs)
print(set_numbirs)

# si quiero convertir este set único a una lista, lo puedo hacer:
unique_numbers = list(set_numbers)
print (unique_numbers)


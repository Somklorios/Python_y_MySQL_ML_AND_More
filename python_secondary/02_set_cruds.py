set_conuntries = {'col', 'mex', 'bol'}
size = len(set_conuntries)
print(size)

# add, agregamos un elemento al conjunto
set_conuntries.add('pe')
print(set_conuntries)
#que pasa si vuelvo a agregar al peru?
# nada, no se volvera a repetir sin importar las veces que sean 
set_conuntries.add('pe')
print(set_conuntries)


# update, lo que hace es sumar elementos a los existentes
#update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
set_conuntries.update({'ar', 'ecua', 'pe'})
print(set_conuntries)

# remove
#remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
set_conuntries.remove('col')
print(set_conuntries)

#set_conuntries.remove('arg')
set_conuntries.discard('arg')
print(set_conuntries)

set_conuntries.add('arg')
print(set_conuntries)

# limpiar todo el conjunto, lo deja en vacío
set_conuntries.clear()
print(set_conuntries)
print(len(set_conuntries))

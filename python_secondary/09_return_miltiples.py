#------------------ Return -------------------

# funcion para calcular un volumen
def find_volumen(length, width, depth):
  return length * width * depth

result = find_volumen(2,3,6)
print(result)
#--> 36

# funcion para calcular un volumen con valores por defecto
# si no ingresa algun valor, la funcion se ejecuta y toma los valores por asignados por defecto
def find_volumen2(length=1, width=1, depth=1):
  return length * width * depth

result = find_volumen2()
print(result)
#--> 1

# asignar un valor especifico a algun parametro de la funcion
result = find_volumen2(width = 12)
print(result)
#--> 12

# funcion que retorna multiples valores
# retorna una tupla
def find_volumen3(length=1, width=1, depth=1):
  return length * width * depth, width, 'hola'

result = find_volumen3(length = 2)
print(result)
#--> (2, 1, 'hola')

#obtener solo un valor de la tupla devuelta
print(result[0])
#--> 2

# asiganar cada valor de una tupla a una variable
result, width, texto = find_volumen3()
print(result)
print(width)
print(texto)
#--> 1

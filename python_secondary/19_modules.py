
#___________modulos___________

#---modulo para manejo del sistema
import sys 

# ubicacion donde se ejecuta el archivo actual
print(sys.path)


import re
text = "mi numero de telefono es 311 123 213, el codigo del pais es 55, mi numero de la suerte es 7"

result = re.findall("[0-9]+", text)
print(result)
#Esta expresión regular busca lo indicado dentro de [ ]


#_____ modulo para el manejo de horas y fechas_____
import time 
timestamp = time.time()
#hora actual en  formato de computadora
local = time.localtime()
#indica la horal loca
result = time.asctime()
#transforma el formato de hora
print(time)
print(result)

#___modulo para el manejo de listas___
import collections
numbers = [1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 4, 5]
counter = collections.Counter(numbers)
#Devuelve un diccionario con el número de veces que se repite un item dentro de un elemento (frecuencia)
print(counter)

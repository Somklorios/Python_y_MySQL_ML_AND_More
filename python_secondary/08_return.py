# nombre de la funcion, Parametros
#       |                |
def sum_with_range(min, max):
  print(min, max) # <---- siemprese ponen : puntos
  sum = 0 
  for x in range(min, max):  # <------- cuerpo de la funcion
    sum += x 
  return sum  # <---- invocacion

result = sum_with_range(1, 10) 
print(result)   
result_2 = sum_with_range(result, result + 10)    
print(result_2)
#sum_with_range(1, 100)    

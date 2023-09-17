#Para resolver este desafío, debes utilizar la función my_divide, que recibe dos parámetros de entrada que representan los números a dividir. Dentro de esta función, debes implementar la lógica necesaria para capturar la excepción ZeroDivisionError. También, debes retornar un mensaje que diga No se puede dividir por 0 cuando esta excepción ocurra.

#Ejemplo 1:

#Input: 10, 2
#Output: 5.0

def my_divide(a, b):
  try:
    result = a / b
  except ZeroDivisionError as error:
    result = 'No se puede dividir por 0'
  return result
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0


#_____________Si fuera en español_____________

#- Esto para mi tiene más sentido porque se trata de entender la sintaxis y no memorizarla mecanicamente

#Ingles
"""
 try:
      result = a / b
      return result
   except ZeroDivisionError as error:
      return 'No se puede dividir por 0'
"""

#español

"""
intenta:
	resultado = a / b
	entonces retorna resultado
excepto el error de división cero como error:
	entonces retorna 'No se puede dividir entre cero'


"""
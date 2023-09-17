try:
  print(0 / 0)
  assert 1 != 1, 'Uno no es igual que uno'
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola')
print('Hola 2')

# A primera vista podemos pensar que lanzar Excepciones no sirve de nada si al final igual ahí mismo las vamos a rodear de un try-except. 

# Pero es más util cuando estamos creando funciones en modulos que van a ser usadas por otros módulos, funciones que dependiendo del uso que se le de en una u otra parte del código del proyecto tienen que hacerse diferentes validaciones para ese “error”.

# Generar excepciones OBLIGA al equipo a manejarlos porque sino, el proyecto no va a funcionar.
# importa el modulo de statistics de python , el cual  permite realizar operaciones como suma,promedio,media etc. 
from statistics import mean
# capturar los valores correspondiente a cada mes
budgetEnero = int(input('ingrese el presupuesto de enero '))
budgetFebrero = int(input('ingrese el presupuesto de febrero '))
budgetMarzo = int(input('ingrese el presupuesto de marzo '))
# hallar el promedio, dentro de '[]' se puede agregar los valores de los meses separados por comas
mean = mean([budgetEnero, budgetFebrero, budgetMarzo])
# imprime el promedio
print(f'el promedio de los meses es {mean}')

lives = 3
print(type(lives))

age = 12
buget = 100

temperature = 12.12
print(type(temperature))

lives = 2
print(lives)
lives = 1
print(lives)

lives = lives - 1
print(lives)

lives -= 1
print(lives)


number = 4000000000000000000.1000004
print(number)

number_b = 0.000000000000000000000000000001
print(number_b)
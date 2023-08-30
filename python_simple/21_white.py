#Un bucle while permite repetir la ejecución de un grupo de instrucciones mientras se cumpla una condición (es decir, mientras la condición tenga el valor True)

'''
while True:
    print('se ejecuto')
   


counter = 0

while counter < 10:
    counter += 1
    print(counter)

#mientras counter sea menor a 10, el bloque se va a ejecutar    

counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break
    print(counter)
'''    
#mientras counter sea menor a 20, el bloque se va a ejecutar
# pero SI el counter el igual a 15 se DETIENE el ciclo    

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)
#El continue sirve para saltarse ciertas partes del código. Por ejemplo, si quiero hacer un conteo de números hasta el 10, pero no quiero que el 5 sea contado   
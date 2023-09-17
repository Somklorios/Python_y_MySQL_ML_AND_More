#1 #Definir una función llamada 'get_totals' que toma un argumento llamado 'orders' 
def get_totals(orders):
   return [order['total'] for order in orders] #2

def calc_total(totals):
   return sum(totals)


# 2 #Dentro de la función, se utiliza list comprehension para crear una nueva lista. El list comprehension itera a través de cada elemento en la lista 'orders' y extrae el valor asociado con la clave 'total' en cada elemento del diccionario 'order'. Luego, estos valores se colocan en una lista que se devuelve como resultado.   
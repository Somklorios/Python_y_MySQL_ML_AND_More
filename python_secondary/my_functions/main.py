# importamos el modulo my_functions; que tiene funciones dentro
import my_functions

def get_total(orders):
  # definimos la funcion get total que toma el argumento llamado orders
  totals = my_functions.get_totals(orders)
  #La variable totals almacena el resultado de la funcion get_totals del modulo my_functions cuando le pasamos el argumento orders 
  Sum = my_functions.calc_total(totals)
  # la variable sum almacena el resultado de la funcion calc_total del modulo my_functions cuando se le pasa el argumento totals
  return Sum
#la funncion get_total devuelve/return el valor almacenado en la varible sum
  

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
# la variable total almacena el resultado de la funcion get_total con el argumento orders
print(total)


#Llama a una función llamada "get_totals" del módulo "my_functions" y pasa el argumento "orders" a esta función. El resultado se almacena en la variable "totals."
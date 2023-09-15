#________Como Construir Módulos____________
#Para construir módulos debemos tener en cuenta que se deben crear en la misma carpeta a lo cual utilizaremos import para ser llamada en el archivo a trabajar:

#Tenemos un módulo que tiene los datos de la población de 3 paises de Sur America, los cualse vamos a crear en la carpeta app y daremos por nombre utils.py

import utils 


data = [
  {
	'Country': 'Colombia',
	'Population': 500
  },
  {
	'Country': 'Bolivia',
	'Population': 300
  }
  ]

def run():
  keys, values = utils.get_population()
  print(keys, values)

  country = input("type country =>  ")

  result = utils.population_by_country(data, country)
  print(result)

if __name__ == "__name__":
  run()
    
# que es este if?

# este if, es el entry point, que le dice al archivo main.py que si es ejecutado desde la terminal, se ejecute la funcion run(), pero si es ejecutado desde otro archivo, esto no se ejecutara.


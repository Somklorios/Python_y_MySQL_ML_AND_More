#________Como Construir Módulos____________
#Para construir módulos debemos tener en cuenta que se deben crear en la misma carpeta a lo cual utilizaremos import para ser llamada en el archivo a trabajar:

#Tenemos un módulo que tiene los datos de la población de 3 paises de Sur America, los cualse vamos a crear en la carpeta app y daremos por nombre utils.py

import utils 
import read_csv
import charts


def run():
  data = read_csv.read_csv('./data_main/data.csv')
  country = input("type country =>  ")
  
  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)


  print(result)

if __name__ == "__name__":
  run()
    
# que es este if?

# este if, es el entry point, que le dice al archivo main.py que si es ejecutado desde la terminal, se ejecute la funcion run(), pero si es ejecutado desde otro archivo, esto no se ejecutara.


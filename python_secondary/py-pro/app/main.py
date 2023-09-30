#________Como Construir Módulos____________
#Para construir módulos debemos tener en cuenta que se deben crear en la misma carpeta a lo cual utilizaremos import para ser llamada en el archivo a trabajar:

#Tenemos un módulo que tiene los datos de la población de 3 paises de Sur America, los cualse vamos a crear en la carpeta app y daremos por nombre utils.py

import utils 
import read_csv
import charts
import pandas as pd

def run():
  '''
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))

  '''

  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'Africa']

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)
  
  data = read_csv.read_csv('data.csv')
  country = input('Type Country => ')
  print(country)


  result = utils.population_by_country(data, country)

  if len(result) >  0:
    country = result[0]
    print(country)
    labels, values =  utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
  run()
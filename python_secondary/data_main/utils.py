def get_population():
   population_dict = {
      '2022': int(population_by_country['2022 Population']),
      '2020': int(population_by_country['2020 Population']),
      '2015': int(population_by_country['2015 Population']),
      '2010': int(population_by_country['2010 Population']),
      '2000': int(population_by_country['2000 Population']),
      '1990': int(population_by_country['1990 Population']),
      '1980': int(population_by_country['1980 Population']),
      '1970': int(population_by_country['1970 Population'])
   }
   labels = population_by_country.keys() 
   values = population_by_country.values()
   return labels, values

def population_by_country(data, country):
    result = list(filter(lambda item: item["Country"] == country, data))
    return result

# tengo un alista con diccionarios
#data es una lista
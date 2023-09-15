def get_population():
    keys = ["mex", "bol"]
    values = [300, 400]
    return keys, values


def population_by_country(data, country):
    result = list(filter(lambda item: item["Country"] == country, data))
    return result

# tengo un alista con diccionarios
#data es una lista

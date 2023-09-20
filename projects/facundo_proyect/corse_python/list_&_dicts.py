def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Sergio", "lastname": "Juarez"}

    super_list = [
        {"firstname": "Sergio", "lastname": "Juarez"},
        {"firstname": "Alfredo", "lastname": "Palacios"},
        {"firstname": "Osvaldo", "lastname": "Garcia"},
        {"firstname": "Rebeca", "lastname": "Soria"},
        {"firstname": "Karla", "lastname": "Pavon"}
    ]

    super_ditc = {
        "natural_numns": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, -3, -4, -5],
        "flotating_nums": [1.1, 4.5, 3.4, 6.43]
    }

    for key, value in super_ditc.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()
# es nuestro entry point
# aqui incializamos la funcion
def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0:
    #        my_dict[i] = i ** 3
    # con dictionary comprehension usamos {} en lugar de [] 

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # para cada elemento en el iterable yo voy a colocar una llave y un valor solamente si se corresponde la condicion

    print(my_dict)   

    print("*" * 80)


    #_________reto________
    # crear, un dictionary comprehension, un dictionario cuyas llaves sean los primeros 1000  numeros con sus raices cuadradas como valores

    mr_dictson = {i: i**0.5 for i in range(1, 1001)}
    print(mr_dictson)

if __name__ == '__main__':
    run()        
def run():
    # squares = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #        squares.append(i ** 2)

# para comentar todo un codigo es "crtl + tecla de }"
    squares = [ i **2 for i in range(1, 101) if i % 3 != 0]

    #          element for  element in iterable if conditional
    # para cada elemento en el iterable yo voy a guardar ese elemento solo si se cumple la condicion
    print(squares)   

if __name__ == '__main__':
    run()



#___________RETO_____________
# crear, con un list comprehension, una lista de todos los multiplos de 4 que a la vez tambien son multiplos de 6 y 9, hasta 5 digitos

list = [ i for i in range(1, 10000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
print(list)
#Higher order function: una función dentro de otra función
#Una función de Orden Superior o en sus siglas HOF se le lama así solo cuando contiene otras funciones como parámetro de entrada o devuelve una función como salida, es decir que en este caso las funciones que operan a otras funciones se les denomina Higher order function.

#También hay que entender que a estas Funciones de Orden Superior HOF se aplican para funciones y métodos que toman como funciones a los parámetros o devuelven una función como un resultado.



def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1

def high_ord_func(x, func):
    return x + func(x)

high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func(2, increment)
# 2 + (2 + 1)
print(result)

result = high_ord_func_v2(2, increment_v2)
print(result)

result = high_ord_func_v2(2, lambda x: x + 2)
print(result)
result = high_ord_func_v2(2, lambda x: x * 2)
print(result)



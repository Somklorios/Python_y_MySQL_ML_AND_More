"""
for element in range(20):
    print(element)
"""
#      Cúando usar “while” o “for” ?
#while: cuando no nonozcas la cantidad de elementos a recorrer o la cantidad de iteraciones a realizar.

#for: cuando conozas la cantidad de elementos a recorrer o el número de iteraciones a relaizar.    

my_list = [23, 45, 67, 89]
for element in my_list:
    print(element)

my_tupla = ("nico", "juli", "santi")
for element in my_tupla:
    print(element) 


product = {
    "name" : "camisa",
    "price" : 100,
    "stock" : 89,
}

for key in product:
    print(key, "=>", product[key])

#forma mas sencilla
for key, value in product.items():
    print(key, "=>", value)

people = [
    {
        'name': 'nico',
        'age': '34'
    },
    {
        'name': 'zule',
        'age': '45'
    },
    {
        'name': 'santi',
        'age': '54'
    }
]

for person in people:
    print('name =>', person['name'])
#Scope o Alcance, es cuando una variable solo esta disponible desde donde fue construida y para ello existen dos ambitos, el local y el global.

#cope Local
#Cuando una variable es construida dentro de una función pertenece al ámbito local de esa función y solo se puede usar dentro de esa función.

price = 100  # global

def increment():
    price = 200
    price = price + 10
    print(price)
    return price

print(price)   
price_2 = increment() 
print(price_2)
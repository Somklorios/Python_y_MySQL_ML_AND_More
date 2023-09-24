# por comodidad podemos importar la informacion de un modulo y la funcion
from DATA import DATA

def run():
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    #___________________________________________________________________________________________________________
    #lista; all_python_devs,que contiene a todos los trabajadores 

    # worker:nombre que le voy a poner a cada uno de las partes de los dictionarios internos

    #name: aqui voy a guardar el contenido de la llave name, valor, osea el nombre de la persona
    
    # de todos lo trabajadores en DATA voy a guardar en NAME de ester trabajador/worker solamente si el lenguaje que domina es python
    #__________________________________________________________________________________________________________

    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
    
    # de todos lo trabajadores en DATA voy a guardar en NAME de ester trabajador/worker solamente si pertenecen a Platzi
    
    #__________________________________________________________________________________________________________

    adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    # voy a guardar a los worker siempre que worker; age, sea mayor a 18, sacando eso de DATA, todo esto va dentro de la funcion filtery a su vez dentro de la funcion list
    # este resultado es mas o menos lo esperado, nos imprime casi todo el diccionario, necesitamos solo nombres
    #__________________________________________________________________________________________________________
    
    #                              combinar order funcions
    adults = list(map(lambda worker: worker["name"], adults))
    #Vamos a aplicar MAP en lugar de filter, vamos a usar worker y de worker solo vamos a usar name y esta vez ya no viene de DATA si no de adults, la variable anterior
    # estamos sobre escribiendo la variable

    # aplicar map sobre todos los diccionarios que contienen worker, extrayendo el valor de la llave name

    #__________________________________________________________________________________________________________
    
    old_people = list(map(lambda worker: worker | { "old": worker["age"] > 70}, DATA))
    # estamos transformando a cada uno de los diccionarios que tenemos en un nuevo diccionario que es la combinacion del diccionario original con uno nuevo
    # | es un nuevo feature, su funcion es unir a un diccionario con uno nuevo
    #si yo al evaluar que la edad es mayor a 70 el resultado es true
    #Para cada uno de los trabajadores  que estan dentro de data, para cada uno de los diccionarios, voy a guardar un nuevo diccionario pero sumando a un diccionario nuevo que contiene la llave old con el valor de valor la expresion worker age, si es mayor de 70 guarda TRUE



    # for worker in all_python_devs: 
    #ciclo: para cada trabajador en la lista all_python_devs
    #     print(worker)

    # for worker in all_Platzi_workers: 
    #     print(worker)
    for worker in adults:
        print(worker)




if __name__ == '__main__':
    run()

import matplotlib.pyplot as plt

#plt es un alias para matplotlib.pyplot

# funcion para grafico de barra
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots() #son dos valores que nos da la librería, fig es como la figura y ax se refire a las coordenadas donde  vamos a empezar a graficar
  ax.bar(labels, values) #aquí le estás indicando pque quieres generar una gráfica de barras (bar), y le envías labels y values para que sepa que tiene que crear el gráfico con esos valores
  plt.savefig('./imgs/' + name + '.png') #es para que nos pide que muestre la gráfica
  plt.close()


# funcion para pie chart
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels) #Aquí le estamos indicando que queremos que nos muestre una gráfica de torta, fijate que en el anterior pusimos un bar y no un pie.
                                #Ahora le indicamos los labels pero también tenemos que indicarle como van a ser los labels 
  ax.axis('equal')
  plt.savefig('pie.png') # Guarda el archivo
  plt.close()


# ejecutar archivo como script desde la terminal
if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100, 40, 800]
  #son los valores y los labels que tendrá la gráfica
  generate_bar_chart(labels, values)
    #Llamando a la función
  generate_pie_chart(labels, values)
    #Llamamos a la función pie chart

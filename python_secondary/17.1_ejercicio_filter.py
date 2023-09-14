#Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para filtrar una lista de palabras, retornando una lista solo con las que cumplan con la condición de tener 4 o más letras.

#La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.

#Ejemplo 1:

#Input: ['amor', 'sol', 'piedra', 'día']
#Output: [ 'amor', 'piedra' ]

def filter_by_length(words):
   # Escribe tu solución 👇
   new_words = list(filter(lambda new_words: len(new_words) >= 4, words))
   return new_words

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)


print (" *  " * 25)

# list
words = ['amor', 'sol', 'piedra', 'día']
#cuenta el numero de elementos de words
print(f'List number of words \n{len(words)}')

#realiza un for que cuenta la candidad de letras en la lista words y realiza un append a la lista numbers_wods
numbers_letters = []
for i in words:
    numbers_letters.append(len(i))    
print(f'List number letters in numbers_letters\n{numbers_letters}')

#list comprehension del paso anterior
numbers_letters_v2 = [len(i) for i in words]
print(f'List number letters in numbers_letters_v2 \n{numbers_letters_v2}')

#utilizar filter y lambda para el paso anterior 
def filter_by_length(words):
    numbers_letters_v3 = list(filter(lambda i:len(i) >= 4, words))
    return numbers_letters_v3

print(f'Result of filter_by_length \n{filter_by_length(words)}')
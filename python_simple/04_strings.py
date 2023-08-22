name = "Sergio"
last_name = "Juarez"
full_name = name + " " + last_name
print(full_name)

quote = "I'm Sergio" 
print(quote)

quote2 = "She say 'Hello' "
print(quote2)

# format

#El formato ayudar a facilitar su impresion en pantalla y no evita estar abriendo y cerrando llaves
template = "Hola perros, mi nombre es " + name + " y mi apellido es " + last_name
print("v1 ", template)

templeta = "Hola, mi nombre es {} y mi apellido es {}" .format(name, last_name)
print("v2", templeta)

templato = f"Hola mi nombre es {name} y mi apellido es {last_name}"
print("v3", templato)
#la f es de format, simplificando mas el formato 
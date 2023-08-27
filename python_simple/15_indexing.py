text = "Culo si no amix jajaj"
print(text)
print(text[1])

size = len(text)
print("size --", size)
print(text[size -1])
print(text[-1])

#slicing
print(text[0:5])
#quiero sacar todo el texto pero desde un lugar especifico
print(text[:10])

print(text[6:-1])

print(text[5:])

print(text[:])

#saltos con el slicing
print(text[8:13:3])
# Fernando Rodríguez López
# 236w0341
# Estructura de Datos 303A
# 12/09/2024

# Ejemplo de listas

lista1 = ["cheetos", 50, "coca", 80, "pepsi", 100, "suavitel", 500, "sabritas", 30, "boing", 300, "tortillinas", 40]
lista2 = ["whirlpool", 1050, "LG thinkq", 8000, "apple vision pro", 16500, "consola switch", 8500]
lista3 = ["resident evil", 1000, "mario 64", 1000, "karlii", 700, "fifa25", 1000]

# Agregar elementos a lista1
lista1.append("boing")
lista1.append(16)
lista1.append("tortillinas")
lista1.append(32)

# Agregar elementos a lista2
lista2.append("LG")
lista2.append(2)
lista2.append("Switch")
lista2.append(5)

# Agregar elementos a lista3
lista3.append("fifa25")
lista3.append(5)
lista3.append("karlii")
lista3.append(3)

# Impresión de las listas
print("Impresión de la lista uno:")
for elemento in lista1:
    print(elemento)
print()  

print("Impresión de la lista dos:")
for elemento in lista2:
    print(elemento)
print() 

print("Impresión de la lista tres:")
for elemento in lista3:
    print(elemento)
print()  

# Eliminación de elementos
try:
    lista1.remove("boing")  # Intentar eliminar un valor que puede estar en la lista
    lista1.remove(16)
    lista1.remove("tortillinas")
    lista1.remove(32)
except ValueError as e:
    print(f"Error al eliminar de lista1: {e}")

try:
    lista2.remove("LG")
    lista2.remove(2)
    lista2.remove("Switch")
    lista2.remove(5)
except ValueError as e:
    print(f"Error al eliminar de lista2: {e}")

try:
    lista3.remove("fifa25")
    lista3.remove(5)
    lista3.remove("karlii")
    lista3.remove(3)
except ValueError as e:
    print(f"Error al eliminar de lista3: {e}")

# Impresión de las listas después de eliminación
print("Impresión de la lista uno después de eliminar:")
for elemento in lista1:
    print(elemento)
print()  

print("Impresión de la lista dos después de eliminar:")
for elemento in lista2:
    print(elemento)
print() 

print("Impresión de la lista tres después de eliminar:")
for elemento in lista3:
    print(elemento)
print()  

#Metodos diccionario

#Keys() -> devuelve las claves (tambien nos sirve para iterar)
#get() -> devuelve el valor de una clave
#clear() -> elimina todos los elementos
#pop() -> elimina un elemento
#items() -> para iterar el dict

diccionario = {
    "nombre" : 'javier',
    "apellido" : 'pulido',
    "money" : 1000000
}

#Nos devuelve un objeto con dict_item
claves = diccionario.keys()

#Obteniendo un elemento con get() (si no encuentra nada el programa continua)
valor_de_elemento = diccionario.get("Hola")
print(claves)

#eleminando todo el diccionario
#diccionario.clear()

#eliminando un elemento dle diccionario
diccionario.pop("nombre")
print(diccionario)

#Obteniendo un elemento dict_items iterable (devuelve el diccionario)#Iterable
diccionario_iterable = diccionario.items()
print(diccionario_iterable)
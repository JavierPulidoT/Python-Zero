diccionario = {
    "nombre" : "Javier",
    "apellido" : "Pulido",
    "subs" : 100000
}
#Recorriendo diccionario para obtener las claves
for key in diccionario:
    key
    print(f"la clave es {key}")


#Recorriendo diccionario con items() para obtener las claves y el valaor

for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")
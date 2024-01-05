#1)Lista (se puede modificar los datos)
list = ["Javier","Pulido",True,20]
print(list)

list[0] = "alejo"
print(list[0])
print(list[1])

#2)Tuplas...los datos de los indices no se pueden modificar
tupla = ("Javier","Pulido",True,20)

#tupla[3] = "Alejandro"

#3)Conjuto (set) - datos desordenamos
conjunto = {"javier","hola",10}
#no se puede modificar un elemento
#No se accede a los elelmntos por indice
#no muestra o almacena datos duplicados
print(conjunto)

#4)diccionario (dict) , key : valor
diccionario ={
    'nombre' : "javier",
    'activo' : True,
    'color' : "azul" 
}

diccionario2 ={
    0 : "javier",
    1 : True,
    2 : "azul" 
}

print(diccionario['nombre'])
print(diccionario2[2])


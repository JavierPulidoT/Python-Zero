#METODOS LIST

#Creando una lista con List()
lista = list(["Hola","como","estas",85])

#Devuelve la cantidad de elementos de la lista
#LEN
cantidad_elementos = len(lista)
print(cantidad_elementos)

#Agregando elementos a la lista
#APPEND = Agrega un elemento a la lista
#INSERT = Agrega un elemento de una lista en el indice especificado
#EXTEND = Agrega varios elementos a la lista

lista.append("jajaja")
print(lista) 

lista.insert(2,"prueba") #indice
print(lista) 

lista.extend([False,"J", 2024])
print(lista) 

#*******************************************************************************
#Eliminar elementos de la lista
#POP = Elimina un elemento de una lista, pide indice y devuelve valor
#REMOVE = Remueve un elemento de una lista, pide valor
#CLEAR = Elimina todos los elementos de una lista

lista.pop(4) #-1 elimina el ultimo indice, -2 antepenultimo...
print(lista) 

lista.remove("jajaja")
print(lista) 

lista.clear()
#print(lista) 

#*******************************************************************************
#Ordenar elementos
#SORT = Ordena una lista de forma ascendente a descendente
#REVERSE = Invierte los elementos de una lista

listaOrden = list([5,8,9,6,44,33,5,18,22,105])

listaOrden.sort()
print(listaOrden)

listaOrden.reverse()
print(listaOrden) #la revierte , no ordenada

listaOrden2 = list([4,8,6,3,8,22,459,62])
listaOrden2.reverse()
print(listaOrden2)

#***********
#Con DIR , podemos ver que podemos hacer con cada metodo
#***********
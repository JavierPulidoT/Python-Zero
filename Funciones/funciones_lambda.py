#Funcion Lambda

multiplicar_por_dos = lambda x : x*2
print(multiplicar_por_dos(5))

#creando funcion para saber si es par o no

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

numeros_pares = filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))
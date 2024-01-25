#ITERAR CONJUNTOS
animales = {"gato" , "perro", "loro" , "cocodrilo"}

numeros = {52,15,23,55}

for animal in animales:
    print(f'Ahora la variable animal es: {animal}')
    
    
for numero in numeros:
    resultado = numero * 10 
    print(resultado)    
    
    
#Para iteral 2 Conjuntos, ambas deben tener la misma cantidad de elementos  (zip)
for numero,animal in zip(animales,numeros):
    print(f'recorriendo Conjunto 1: {animal}')
    print(f'recorriendo Conjunto 2: {numero}')
    
  
#forma correxta de recorrer una Conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#Usando el else
for numero in numero:
    print(f'ejecutando el ultimo bucle, valor actual {numero}')     
else:
    print("el bucle terminó")    
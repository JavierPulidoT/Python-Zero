#ITERAR
animales = ["gato" , "perro", "loro" , "cocodrilo"]

numeros = [52,15,28,32]

for animal in animales:
    print(f'Ahora la variable animal es: {animal}')
    
    
for numero in numeros:
    resultado = numero * 10 
    print(resultado)    
    
    
#Para iteral 2 listas, ambas deben tener la misma cantidad de elementos  (zip)
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista 1: {animal}')
    print(f'recorriendo lista 2: {numero}')
    
#forma no optima de recorrer una lista con su indice    
for num in range(len(numeros)):
      print(numeros[num])
      
#forma correxta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#Usando el else
for numero in numero:
    print(f'ejecutando el ultimo bucle, valor actual {numero}')     
else:
    print("el bucle terminó")    
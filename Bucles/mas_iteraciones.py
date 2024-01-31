
frutas = ["banana", "manzana", "pera", "durazno"]
cadena = "Hola Como estas"
numeros = [2,8,5,10]


#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f"Me voy a comer una {fruta}")
    
#evitando que el bucle siga ejecutansose
for fruta in frutas:
        print(f'Me voy a comer una {fruta}')
        if fruta == 'pera':
            break
    
print("bucle terminando")

#Recorrer una cadena de texto

for letra in cadena:
    print(letra)
    
#(duplicamos los numeros)
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)
    
    print(numeros_duplicados)
    
 #Bucles for en una sola linea de codigo   (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
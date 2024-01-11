#Ejercicio 1.2
#A) Pedirle al usuario que diga cualquier texto real y:
    #Pedirle cuanto tardaria en decir esa frase
    #Cuantas palabras dijo?
    
#B)Si se tarda mas de 1 minuto
    #Decirle "frase muy larga"
   
#C)David habla un 30% mas rapido...
    #Cuanto tardaria el en decirlo?    
    
#***************************************************************
  
frase = input("Ingresa una frase, y te calculo cuando tardarias en decirla: ")
print("--------------------------")
palabras_separadas =  frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Escribiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras / 2} segundos en decirlo')
print("--------------------------")
print(f'David tardaria {cantidad_de_palabras * 100 // 2 *1.3} segundos en decirlo')
print("--------------------------")
if (cantidad_de_palabras > 120):
    print("Frase muy larga, no es un testamento")
#Falto el profe

#Pedir el nombre y edad de los compañeros que vinieron a clases

def obtener_compañeros(cantidad_de_compañeros):
    
    #Creando la lista con los compañeros
    compañeros = []
        
        #Ejecutando un For para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
            nombre = input("Ingrese el nombre del compañero: ")
            edad = input("Ingrese la edad del compañero: ")
            compañero = (nombre,edad)
            
            #Agregando la informacion a la lista
            compañeros.append(compañero)
            
    #Ordenandolos de menor a mayor segunedad
    compañeros.sort(key=lambda x:x[1])
    
    #Compañerps[x] devuelven una tupla con (nombre,edad) y despues accedemos al nombre
    #Para definir al asistente y al profesor
    asistente = compañeros[0][0]
    profesor = compañeros[0][0]
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)   
    
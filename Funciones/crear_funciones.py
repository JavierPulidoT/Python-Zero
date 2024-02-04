#Creando una funcion simple

#def saludar():
#    print("Hola como estas?")
    
#saludar()

#Funcion con parametro
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "rey"
    else:
        adjetivo = 'amor'
    
    print(f"Hola {nombre}, mi {adjetivo} ¿como estas?")
    
    saludar("camila","mujer")
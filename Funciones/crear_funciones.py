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
    
#Crear una Funsion que me devuelva valores
def crear_contraseña_random(num):
    chars = "abcdefghijk"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num 
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{(num*2)}"
    return(contraseña)
    
password = crear_contraseña_random(4)    
frase = f"Tu contraseña nueva es: {password}"
print(frase)
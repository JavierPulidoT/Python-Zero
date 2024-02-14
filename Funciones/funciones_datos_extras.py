#Funcion 3 parametros

def frase(nombre,apellido,adjetivo):
    return f'Hola {nombre} {apellido} , eres muy {adjetivo}'

#Utilizando keyword arguments
frase_resultante = frase(adjetivo = "Grande",nombre = "Juan" , apellido = "Perez")

print(frase_resultante)



#Redefinir variable, misma funcion con valor opcional y un parametro por defecto
def frase(nombre,apellido,adjetivo = "Inteligente"):
    return f'Hola {nombre} {apellido} , eres muy {adjetivo}'

frase_resultante = frase(adjetivo = "Grande",nombre = "Juan" , apellido = "Perez")

print(frase_resultante)
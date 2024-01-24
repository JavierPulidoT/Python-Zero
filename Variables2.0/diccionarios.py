#Creando diccionarios con dict(), puiede ser vacio con la funcion dict
diccionario = dict(nombre = "javier" ,apellido="Pulido")

#diccionario con datos
diccionario ={
    'nombre' : "Javier",
    'apellido' : "Pulido",
    'color' : "azul" 
}
#Las listas no pueden ser claves si usamos forzentset para meter conjuntos
diccionario = {frozenset(["Javier", "Pulido"]) : "Hola"}

#Creando diccionarios con fromkeys(), valores vacios sin definir, CON DOS PARAMETROS
diccionario = dict.fromkeys(["nombre", "apellido"]) #nombre : None

diccionario = dict.fromkeys("ABCDE")

#Creando diccionarios con fromkeys(), cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")



print(diccionario)
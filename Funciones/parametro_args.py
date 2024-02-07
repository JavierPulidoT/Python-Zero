#Forma No optima de sumar valores
#def suma(lista):
#    numeros_sumados = 0
#   for numero in lista;
#        numeros_sumados = numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,3,9,10,20,3])    

#Utilizando el parametro args
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("Lucas",5,3,6,9,88,4)
print(resultado)
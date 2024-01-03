a = 2   #int
b = 3.2  #float
c = a + b
x = True   #boolean
print(c)

#Definiendo variable con camelCase.
nombreCompleto = "Javier Pulido"


#Definiendo variable con snake_case... recomendado para python.
nombre_completo_1 = "Javier Pulido"

#Concatenar com +
n = 'Javier'
bienvenida = "Hola " + n + " Como estas?"
print(bienvenida)

#Concatenar con f-string
#todo lo que este en f{} lo convierte en texto
n2 = 'Javier'
bienvenida2 = f"Hola  {n2}  Como estas?"

#Dejar declarar una variable
#del bienvenida2

print(bienvenida2)

#Operadores de pertenencia (in / not in) 
print("Hola" in bienvenida2) #true
print("Hola" not in bienvenida2) #false

#Operadores de identidad
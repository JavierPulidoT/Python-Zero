#METODOS
#DATO.metodo()
#********************************************
#DIR es una funcion de pyton > ver que se puede hacer con ese dato"objeto"
#UPPER = Convierte a mayuscula
#LOWER = Convierte a minusculas
#CAPITALIZE = Primera a Mayuscula
#
#FIND = metodo encuentra la primera operacion del valor especificado, sino devuelve "1"
#INDEX = metodo encuentra la primera aparicion del valor especificado, sino devuelve una excepcion
#
#ISNUMERIC = si es numerico devuelve "True"
#ISALPHA = si es alfa-numerico devuelve "True"
#
#COUNT = devuelve el numero de ocurrecnias de una subcadena en la cadena dada
#LEN  = cuenta los caracteres de una cadena , es funcion
#
#ENDSWITH = verifica si una cadena termina con...
#STARTSWITH = verifica si una cadena comienza con... 
#
#REPLACE =  Remplaza un valor por otro
#SPLIT = Separa por el parametro dato
#********************************************
cadena1 = "Holacomoestas"
cadena2 = "Bienvenidos"

#resultado = Upper(cadena1) error
#los metodos son seguidos de 
mayusculas = cadena1.upper() #HOLA

minusculas = cadena1.lower()

primera_letra_mayuscula = cadena1.capitalize()

busqueda_find = cadena1.find("l") #devuelve el indice, sino considencia -1

busqueda_index = cadena1.index("o")#sino hay considencia lanza una excepcion

es_numerico = cadena1.isnumeric()

es_alpha = cadena1.isalpha() #solamente son validos caracteres de A-Z, No espacios

contador = cadena1.count("a")

cantidad_caracteres = len(cadena1) #len es funcion

empieza_con = cadena1.startswith("H")

termina_con = cadena1.endswith("a")

replace = cadena1.replace("la" , "lu")

cadenaseparar = "Hola,como,estas"
separar = cadenaseparar.split(",")

print(separar)



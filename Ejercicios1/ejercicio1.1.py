#Ejercicios
#A)Diferencia en porcentaje entre Maquina(produccion) actual,
    #la maquina mas rapida de la fabrica
    #la maquina mas lenta  de la fabrica
    #el promedio de las maquinas de la fabrica
    
#B) Procentaje de horas (trabajadas) que se reduce en:
    #el promedio de las maquinas
    #la maquina actual(Nueva)
    
#C)10 horas de proccion de la maquina nueva, a cuantas horas del las otras maquinas equivale y al reves...   
    
otras_maquinas_min = 2.5
otras_maquinas_max = 7
otras_maquinas_promedio = 4 
nueva_maquina = 1.5

#horas trabajadas maquina
h_trabajadas_promedio = 5
h_trabajadas_nueva = 3.5

#Ejercicio A

diferenciaa_con_min = 100 - nueva_maquina / otras_maquinas_min * 100
diferencia_con_max = 100 - nueva_maquina * 1000 // otras_maquinas_max / 10
diferencia_con_promedio = 100 - nueva_maquina / otras_maquinas_promedio * 100

#Mostrando la diferencia de horas trabajadas
print("La maquina nueva dura:")
print(f' - un {diferenciaa_con_min}% menos que la maquina mas rapida')
print(f' - un {diferencia_con_max}% menos que la maquina mas lenta')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print("--------------------------")
#Ejercicio B

#Calculando el pricentaje de tiempo perdido
tiempo_perdido_promedio = 100 - otras_maquinas_promedio * 1000 // h_trabajadas_promedio /10
tiempo_perdido_maquina_nueva = 100 - nueva_maquina * 1000 // h_trabajadas_nueva / 10 

#Mostrando la cantidad de horas perdidas 

print(f'La maquina tiene un {tiempo_perdido_promedio}% de tiempo perdido')
print(f'La maquina nueva elimino el {tiempo_perdido_maquina_nueva}% del tiempo perdido')
print("--------------------------")

#Ejercicio C

#Mostrando diferencia si las maquinas trabajaran 10h
print(f'10 horas trabajas(producidas) de la maquina nueva equivalen a {otras_maquinas_promedio * 100 // nueva_maquina / 10} horas de otras maquinas')
print(f'EL trabajo de 10h de las otras maquinas, equivalen a {nueva_maquina * 100 // otras_maquinas_promedio / 10} horas de la maquina nueva')
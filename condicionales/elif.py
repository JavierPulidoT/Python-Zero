ingreso_mensual = 81000
gasto_mensual = 80000

#if anidados y elif

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficid")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estas bien")
    else:
         print("estas gastando mas de lo adecuado")        
    
elif ingreso_mensual > 1000:
    print("estas bien en LATAM")
else:
    print("Eres pobre")
    
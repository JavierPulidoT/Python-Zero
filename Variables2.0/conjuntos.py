#Creando conjunto con Set()

conjunto = set(["dato1", "dato2"]) #lista

#Metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}

print(conjunto2)


#Teoria de Conjuntos

conjuntoA = {1,3,5,7}
conjuntoB = {1,3,7}

#issubset, "es un subconjunto?" == <=
resultado = conjuntoA.issubset(conjuntoB)
#resultado = conjuntoA <= conjuntoB
resultado2 = conjuntoB.issubset(conjuntoA)

print(resultado)
print(resultado2)

#issubset, "es un superconjunto?" == >
#resultado3 = conjuntoA.issuperset(conjuntoB)
resultado3 = conjuntoA > conjuntoB
resultado4 = conjuntoB.issuperset(conjuntoA)

print(resultado3)
print(resultado4)

#Verificar si hay algun numero en comun
resultado_comun = conjuntoA.isdisjoint(conjuntoB)
print(resultado_comun)

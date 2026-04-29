lista  = [100,3,5,10,15,20]
menor_valor = lista[0] 

for n in lista:
    if n < menor_valor:
        menor_valor = n

print(menor_valor)
numero = int(input("Digite um numero: "))
divisoes = 0 
contador = numero

while contador > 0:
    if numero % contador == 0 :
        divisoes += 1

    contador -= 1

if divisoes == 2:
    print(f'{numero} É primo')
else:
    print(f'{numero} Não é primo')
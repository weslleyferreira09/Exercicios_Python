valor = int(input('Quanto voçê quer sacar: '))
nota_100 = 0
nota_50 = 0 
nota_20 = 0 
nota_10 = 0
nota_1 = 0
saque = valor

while saque > 0 :
    while saque >= 100:
        nota_100 = nota_100 + 1
        saque = saque - 100
    while saque >= 50 :
        nota_50 = nota_50 + 1
        saque = saque - 50
    while saque >= 20 :
        nota_20 = nota_20 + 1
        saque = saque - 20
    while saque >= 10 :
        nota_10 = nota_10 + 1
        saque = saque - 1
    while saque >= 1 :
        nota_1 = nota_1 + 1
        saque = saque - 1

print(f'Voçê vai receber {nota_100} de R$100 , {nota_50} nota de R$50, {nota_20} notas de R$20,{nota_10} notas de R$10 e {nota_1} notas de R$1 ')
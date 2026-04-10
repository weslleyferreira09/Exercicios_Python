salario = float(input('Digite o valor do seu salario: '))
aumento = float(input('Digite a porcetagem : '))

print(salario)
print(aumento)

novo_salario = salario + (salario * (aumento/100))

print(f'Seu novo salario e de R$ {novo_salario}')
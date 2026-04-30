carro = {
    'Pneus': 4,
    'Portas':2,
    'Motor':1,
    'Janelas':4
}

print(carro)

carro['Teto_Solar'] = 1

print(carro)

del carro['Motor']
del carro['Janelas']
print(carro)
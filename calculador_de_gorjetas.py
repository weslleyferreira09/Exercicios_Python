gorjeta = 0
quantidade_pessoas = 0
valor_conta = 0

comanda = {
    'Hamburguer': 35.00,
    'Batata-Frita': 20.00,
    'Refrigerante': 8.50,
    'Sobremesa': 15.00
}


print('---EXTRATO DA CONTA ---')

for produto, preco in comanda.items():
    print(f'{produto}: R$ {preco:.2f}')
    valor_conta = valor_conta + preco
if valor_conta >= 200:
    valor_conta = valor_conta * 0.90
    print('Parabens voce ganhou 10% de desconto por causa do  valor da conta')
while gorjeta not in [10, 12, 15]:
    gorjeta = int(input('Qual o valor da Gorjeta(10, 12 ou 15): '))
    if gorjeta not in [10, 12, 15]:
        print('Opção invalida!!! Escolha apenas [10,12,15]')
while quantidade_pessoas <= 0:
    quantidade_pessoas = int(
        input('A conta será dividida para quantas pessoas?'))
    if quantidade_pessoas <= 0:
        print('Erro !!! O numero de pessoas deve ser pelo menos 1.')

total = valor_conta + (valor_conta * gorjeta/100)

valor_final = total / quantidade_pessoas

print(f'Cada pessoa deve pagar: R${valor_final:.2f}')

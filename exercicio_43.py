perifericos = ['mouse','teclado','monitor','mousepad']
item1 = input('Qual periférico voçê está procurando? ')
item2 = input('Tem outro periférico voçê está procurando? ')

i = 0


while i < len(perifericos):
    if perifericos[i] == item1:
        print(f'O primeiro objeto foi encontrado primeiro! {item1}')
        break
    elif perifericos[i] == item2:
        print(f'O segundo objeto foi encontrado antes! {item2}')
        break

    i = i + 1
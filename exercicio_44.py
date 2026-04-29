pecas_carro = [ 'rodao' ,'pneu' , 'biodo', 'roda']
item = input("Qual item esta procurando? ")

for i in pecas_carro:
    if pecas_carro == item:
        print(f'Temos disponivel o item! {item}')
        break
    else:
        print(f'Não temos disponivel o item! {item}')
        break


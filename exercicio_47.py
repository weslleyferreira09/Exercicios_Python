roupas_a = ['Camisa gola Polo','Azul',50]
roupas_b = ['Bermuda Mauricinho','Cinza',45]
roupas_c = ['Boné','Preto',34]

loja = [roupas_a,roupas_b,roupas_c]

print(loja)

for nome , cor , preco in loja :
    print(f'Roupa:{nome},Cor:{cor} e valor:{preco}')
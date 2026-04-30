livros = {
    'Banco de Dados Implementação em SQL,PL/SQL e Oracle 11g' : 329,
    'Problemas Classicos de Ciências da Computação com Python' : 272
}



print(livros['Banco de Dados Implementação em SQL,PL/SQL e Oracle 11g'])
print(f'Quantas paginas tem o livro Problemas Classicos de Ciências da Computação com Python? {livros["Problemas Classicos de Ciências da Computação com Python"]} paginas')

for livro in livros :
    print(livro)
    print(livros[livro])


#Checando se Chave existe  

print('Problemas Classicos de Ciências da Computação com Python' in livros)


# Adicionando e Deletando Chaves

dic = {}

print(dic)

dic['nome'] = 'Weslley'

print(dic)
print(dic['nome'])

dic['sobrenome'] = 'Ferreira'

print(dic)

del dic['nome']

print(dic)
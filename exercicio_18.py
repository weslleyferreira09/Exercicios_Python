conta = float(359.56)
quantia = float(input('Digite um valor: '))

conta = conta + quantia

fatura = conta - 125.98

print(f"Seu saldo e de R${conta}, voçe recebeu um deposito de R${quantia} e sua fatura do cartao de credito e R$ 125.98 , por tanto foi debitado automaticamente pela sua conta bancaria e seu saldo restante e de R${fatura:.2f}")
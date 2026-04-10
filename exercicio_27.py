renda = int(input("Digite sua renda: "))
print("\n ----- Baseado na sua renda vamos liberar o limite no seu cartão de credito -----")

if renda < 2000 :
    limite = 1000
elif renda < 4000 :
    limite = 2000
elif renda < 10000 :
    limite =  3000
elif renda > 10000 :
    print("Fale com o Gerente para liberar o limite do cartão de credito")
    limite = 4000

print(f"O seu limite é R${limite}")
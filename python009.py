# 9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) 
# e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.

dolar = 5.45 
valor = (float(input("Digite quanto de dinheiro você tem = ")))
quantia_em_dolar = (valor/dolar)
print(f"Você teria um total de {quantia_em_dolar:,.2f} doláres")
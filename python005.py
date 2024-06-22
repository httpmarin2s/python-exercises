print("PROGRAMA DE PROVA DE QUÍMICA" , end="")
lista = []
print("")
qtd = int(input ("Quantas provas você fez? "))
n = 0 
for notas in range(qtd): 
    notas = float(input(f"Digite sua nota: na prova {n+1}: "))
    lista.append(notas)
    n = n + 1 

soma = sum(lista)
iten = len(lista)
media = soma/iten

print(f"Sua média foi {media:.2f}")
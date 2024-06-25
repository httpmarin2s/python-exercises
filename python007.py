def dobro (valor1): 
    valor2 = valor1*2
    return valor2

def terca_parte (valor1): 
    valor2 = valor1/3
    return valor2


numero = (float(input("Digite um número: ")))
dob = dobro(numero)
ter = terca_parte(numero)

print(f" O antecessor desse número é {dob}")
print(f" O sucessor desse numéro é {ter:2f}")
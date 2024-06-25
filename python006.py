
def sucessor (valor1): 
    valor2 = valor1 + 1 
    return valor2

def antecessor (valor1): 
    valor2 = valor1 - 1 
    return valor2


numero = int(input("Digite um número: "))
ant = antecessor(numero)
sup = sucessor(numero)

print(f" O antecessor desse número é {ant}")
print(f" O sucessor desse numéro é {sup}")
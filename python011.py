import numpy as np 
print("Equação de Segundo grau")
print("Molde da equação: Ax² + Bx + C ")

def delta(num1, num2, num3): 
    registro = (num2**2)- (4*num1*num3)
    return registro

numero_aleatorios = np.random.randint(1,101, size=3)
A, B, C = numero_aleatorios

print(f" A sua equação de segundo grau é {A}x² + {B}x + {C}")
print("vamos resolvê-la") 

resultado = delta(A,B,C)
print (f"O valor de delta é igual a {resultado}")



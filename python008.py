# 8) Desenvolva um programa que leia uma distância em metros e mostre os valores 
#    relativos em outras medidas.
#    Ex: 
#    Digite uma distância em metros: 185.72
#    A distância de 85.7m corresponde a:

#    0.18572Km
#    1.8572Hm
#    18.572Dam
#    1857.2dm
#    18572.0cm
#    185720.0mm

def km (num1): 
    num2 = num1/1000
    return num2

def hm (num1): 
    num2 = num1/100
    return num2

def dam(num1): 
    num2 = num1/10
    return num2

def dm (num1): 
    num2 = num1*10
    return num2
    
def cm (num1):  
    num2 = num1*100
    return num2

def mm (num1): 
    num2 = num1*1000
    return num2

m = (float(input("Digite o valor em metros: ")))
km1 = km(m) 
print(f"O valor {m} em Km resulta em = {km1}")

hm1 = hm(m)
print(f"O valor {m} em Hm resulta em = {hm1}")

dam1= dam(m)
print(f"O valor {m} em Dam resulta em = {dam1}")

dm1= dm(m)
print(f"O valor {m} em dm resulta em = {dm1}")

cm1= cm(m)
print(f"O valor {m} em cm resulta em = {cm1}")

mm1= mm(m)
print(f"O valor {m} em mm resulta em = {mm1}")
#biblioteca
from math import sqrt

#calcula hipotenusa
def calcular_hipotenusa(c1,c2):
    h = sqrt((c1**2)+ (c2**2))
    return h

#programa principal

print("CALCULAR HIPOTENUSA")

#Usuário informar os valores dos catetos
c1 = float(input("Informe o valor do 1º cateto: ").replace(",","."))
c2 = float(input("Informe o valor do 2º cateto: ").replace(",","."))

#exibe na tela o valor da hipotenusa
print(f"O valor da hipotenusa é{calcular_hipotenusa(c1,c2)}.")
#Faça um algoritmo que peça 2 números inteiros e um número real. 
#Calcule e mostre 

#a) o produto do dobro do primeiro com metade do segundo .

#b) a soma do triplo do primeiro com o segundo.

#c) o segundo elevado ao cubo.

n1 = int(input("Digite o primeiro número"))

n2 = int(input("Digite o segundo número"))

d = n2 * 2

m = n2 / 2

t = n1 * 3 

el_cubo = n2 * n2 * n2
print(" o produto do dobro do primeiro com metade do segundo é \n", d + m)

print("a soma do triplo do primeiro com o segundo é \n", t + n2)

print("o segundo elevado ao cubo é", el_cubo)
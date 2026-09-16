from ast import Mult
from re import sub
n1 = int(input("Digite o primeiro número\n:"))
n2 = int(input("Digite o segundo número\n:"))

so = n1 + n2
su = n1 - n2

op = (input("Digite o tipo de operação:"))

if (op == "+"):
 print( "O resultado é ", so)

elif (op == "-"):
 print( "O resultado é ", su)

else:
 print("ESSE É UM ALGORÍTMO DE SOMA E SUBTRAÇÃO JUMENTOO")

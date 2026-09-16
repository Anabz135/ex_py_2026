n1 = int(input("Digite o primeiro número\n"))
n2 = int(input("Digite o segundo número\n"))
n3 = int(input("Digite o terceiro número\n"))

if (n1 > n2 and n2 > n3):
 print("\n", n1, "\n", n2, "\n", n3)

elif(n1 > n2 and n3 > n2):
 print("\n", n1, "\n",n3, "\n",n2)

elif(n2 > n1 and n1 > n3):
 print("\n", n2, "\n",n1, "\n",n3)

elif(n2 > n3 and n3 > n1):
 print("\n", n2, "\n", n3, "\n", n1)

elif(n3 > n1 and n1 > n2):
 print("\n", n3, "\n", n1, "\n", n2)

else:
 print("\n", n3, "\n", n2, "\n", n1)
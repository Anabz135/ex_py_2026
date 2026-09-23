#Faça um algoritmo que leia 5 números e informe o maior número.

n1 = int(input("Digite o 1 número:"))
n2 = int(input("Digite o 2 número:"))
n3 = int(input("Digite o 3 número:"))
n4 = int(input("Digite o 4 número:"))
n5 = int(input("Digite o 5 número:"))


if (n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5):
	  print("O número", n1 ," é maior")

elif (n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5):
      print("O número", n2 ," é maior")

elif (n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5):
      print("O número", n3 ," é maior")

elif (n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5):
      print("O número", n4 ," é maior")

elif (n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4):
      print("O número", n5 ," é maior")
        
else:
          print("Os números são iguais")

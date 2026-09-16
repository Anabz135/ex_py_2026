n1 = int(input("Digite o primeiro lado do triângulo\n:"))
n2 = int(input("Digite o segundo lado do triângulo\n:"))
n3 = int(input("Digite o terceiro lado do triangulo\n:"))

if( n1 == n2 and n2 == n3):
  print(" Triângulo equiláreto!")
elif(n1 != n2 and n1 != n3 and n2 != n3):
  print(" Triângulo escaleno")
else:
  print("Triângulo isósceles")
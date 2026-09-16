n1 = float(input(" Digite o 1 número: "))
n2 = float(input(" Digite o 2 número: "))

so = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2

print("\n Soma [1] ou  [+]\n")
print(" Subtração [2] ou [-]\n")
print(" Múltiplicação [3] ou [X]\n")
print(" Divisão [4] OU [/]\n")

esc = str(input(" Digite a conta desejada \n "))





if (esc == "1" or esc == "+"):
	print(" A soma desses números é: ", so)

elif (esc == "2" or esc == "-"):
	print(" A subtração desses números é: ", sub)

elif (esc == "3" or esc == "X" or esc == "x"):
   	print(" A múltiplicação desses números é: ", mul)
 
elif (esc == "4" or esc == "/"):
	print(" A divisão desses números é:  ", div)

else:
	print("Que djabo de conta é essa que eu não disponibilizei aqui meu fio?")


#Faça um algoritmo que leia um número e exiba o dia correspondente da semana. 
#(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = str(input("Digite um número que corresponda a um dia da semana \n:"))

if (dia == "1"):
    print("Domingo")

elif ( dia == "2"):
    print("Segunda")

elif ( dia == "3"):
    print("Terça")

elif ( dia == "4"):
    print("Quarta")

elif ( dia == "5"):
    print("Quinta")

elif ( dia == "6"):
    print("Sexta")

elif ( dia == "7"):
    print("Sabado")

else:
    print("Você tirou esse dia da onde? do calendário maia?")
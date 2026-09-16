#Faça um algoritmo  que calcule seu peso ideal,
#para isso receba a altura (h) de uma pessoa,
#receba o sexo (H para Homens e M para Mulher) 
#e utilize as seguintes fórmulas:

#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7


alt = int (input("Digite sua altura"))

s = int(input("Digite seu sexo \n[M]\n Mulher \n[H]\n Homem"))

cal_h = (72.7*h) - 58

          
if(s == "M" or s == "m"):
	print("", cal_m)

 cal_m = (62.1*h) - 44.7

		
elif (s == "H" or s == "h"):
	print("",  cal_h)

else:
	print("Isso não é um gênero Criatura")
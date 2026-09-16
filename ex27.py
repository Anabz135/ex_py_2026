nas = int(input(" Digite o seu ano de nascimento \n "))
ano = int(input(" Digite o ano \n"))
		
id = (nas - ano)
print(" Você tem", id," anos\n")

meses =  (id * 12)
print(" Você tem", meses," em meses")

dia = (id * 365)
print("\n Você tem", dia ," em dias")

sem = (id * 52)
print("\n Você tem", sem * 52 ," em semanas")

ddn = (2029 - nas)
print("\n você tinha ", ddn ," anos")
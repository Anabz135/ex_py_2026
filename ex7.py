n1 = int(input("Digite a primeira nota\n:"))
n2 = int(input("Digite a segunda nota\n:"))
n3 = int(input("Digite a terceira nota\n:"))
n4 = int(input("Digite a quarta nota\n:"))

disc = str(input("Digite a matéria\n:"))

media = (n1 + n2 + n3 + n4) /4

print(f"Sua média é {media} na matéria {disc}")

if(media > 5):
 print("Você está aprovado")

else:
 print("Estude maissss acefaloooo")
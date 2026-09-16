sa = int(input("Digite seu salário\n"))

gr = sa *5 / 100
imp = sa *7 /100

print(" Seu salário é\n", sa ,"\n Mais sua gratificação de", gr ,"\n menos seu imposto de", imp ,"\n O seu total é\n", sa + gr - imp)
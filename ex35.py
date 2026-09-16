area = int(input("Digite a área a ser pintada (em metros) "))

litros = area/3
latas = litros/18

if(latas *18 < litros):
    
    latas = latas + 1

    valor = latas * 80

print(f"De acordo com a área {area}")
print(f"\n Você precisará de: {latas} latas para pintar a área")
print(f"\n Subtotal de tintas")
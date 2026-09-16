#Faça um algoritmo que peça a temperatura em graus Celsius, 
#transforme e mostre a temperatura em graus Fahrenheit e Kelvin.
#Fahrenheit → (0 °C × 9/5) + 32 = 32 °F (EUA e Inglaterra)
#Kelvin → 0 °C + 273,15 = 273,15 K (Química e Física)

tem = int(input("Digite a temperatura em graus celcius \n"))

#Para converter uma temperatura de graus Celsius para Fahrenheit
#você deve multiplicar o valor em Celsius por 1,8 e somar 32. 

fah = (tem * 1,8 ) + 32 

print("Essa temperatura de celsius pra fahrenheit é = ", fah ,"\n")

#Para transformar graus Celsius em Kelvin, basta somar 273 
#(ou 273,15 para mais precisão) à temperatura em Celsius.

kel = (tem + 273)

print("Essa temperatura de celsius pra kelvin é = ", kel ,"\n")
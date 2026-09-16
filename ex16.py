sa = int(input("Digite seu salário\n"))
per = int(input("Digite o percentual do seu aumento\n"))

aumento = (sa * per) / 100
novo_salario = sa + aumento

print("Valor do aumento: R$ ",aumento)
print("Novo salário: R$ ",novo_salario)
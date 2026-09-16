dep = int(input("Digite seu depósito\n"))
tax = int(input("Digite a taxa de juros\n"))

cal = dep * (tax/100)

print("O valor do rendimento total é ", cal)

print("E o valor total é", cal + dep)
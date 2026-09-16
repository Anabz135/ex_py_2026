n1 = int(input("Digite um número: "))
print(f"\n-- Tabuada do {n1} --\n")

i = 0

#for i in range(0, 11, 2): # range(start, stop+1, step)
for i in range(11): # range(start, stop+1, step)
    print(f'{n1} x {i} = {n1*i}'  )
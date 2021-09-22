p1 = int(input("Insira o primeiro preço: "))
p2 = int(input("Insira o segundo preço: "))

desc1 = (p1/100)*8
desc2 = (p2/100)*11

total = (p1 - desc1) + (p2 - desc2)

print(f"Valor final é R${total}")

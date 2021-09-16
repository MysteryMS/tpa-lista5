p1 = int(input("Insira o primeiro preço: "))
p2 = int(input("Insira o segundo preço: "))

desc1 = (p1/100)*8
desc2 = (p2/100)*11

print(f"Valor final do produto 1: R${p1 - desc1}\nValor final do produto 2: R${p2 - desc2}")

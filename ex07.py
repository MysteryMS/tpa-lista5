n1 = int(input("Insira o primeiro número: "))
n2 = int(input("Insira o segundo número: "))

inter = []

count = n1+1
while count < n2:
    inter.append(str(count))
    count += 1

print(f"Resultado: {' '.join(inter)}")

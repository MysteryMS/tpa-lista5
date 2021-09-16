maior = 0
count = 1

while count <= 10:
    num = int(input(f"Insira o número {count}: "))
    if num > maior:
        maior = num
    count += 1

print(f"O maior o número foi {maior}")

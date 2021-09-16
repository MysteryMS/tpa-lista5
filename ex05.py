numero = int(input("Insira um número: "))
resultado = numero
count = numero

while (count > 1):
    count -= 1
    resultado = resultado * count

print(f"{numero}! é igual a {resultado}")

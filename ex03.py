count = 1
maiores_de_idade = []
while (count <= 10):
    ano = int(input(f"Insira a idade {count}: "))
    if 2021 - ano >= 18:
        maioresDeIdade.append(ano)
    count += 1

print(f"{len(maioresDeIdade)} pessoas são maiores de idade.")

nome = input("Insira o nome: ")

nota1 = int(input("Insira a primeira nota: "))
nota2 = int(input("Insira a segunda nota: "))
nota3 = int(input("Insira a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media > 7:
    print(f"Parabéns, {nome}! Você foi aprovado")
elif media < 7 and media > 5:
    print(f"Você ficou com média {media} e está de recuperação")
elif media < 5:
    print(f"{nome}, você foi reprovado")

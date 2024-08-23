MAIOR_IDADE = 18
IDADE_ESPECIAL = 15

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, o voto é obrigatório")
elif idade < MAIOR_IDADE and idade > IDADE_ESPECIAL:
    print("O voto é facultativo.")
else:
    print("Ainda não pode votar!")
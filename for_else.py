texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

# o FOR funciona em 2 partes:
# 1) No exemplo abaixo, 'texto' é o objeto iterável que eu quero percorrer
# 2) 'letra' o item que eu quero percorrer naquele momento.
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adiciona uma quebra de linha
    print("Executa no final do laço")
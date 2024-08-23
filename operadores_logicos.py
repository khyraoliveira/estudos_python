# AND = para ser True tudo tem que ser True
# OR = para ser True apenas um tem que ser True

saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
print(saque <= limite)

# OPERADOR 'E' ou AND
print(saldo >= saque and saque <= limite) # deu FALSE pq se um for false, a afirmação será false.

# OPERADOR 'OU' ou OR
print(saldo >= saque or saque <= limite) # aqui é TRUE, pq se um for verdade, a afirmação é true.

# Operador de negação 'NOT'

print(not 1000 > 1500) # negação de negação = afirmação, true.

contatos = []
print(not contatos) # uma lista VAZIA é FALSE, a negação disso é TRUE.

print(not "saque 1500") # o valor da string é verdadeiro, sua negação é FALSE.

print(not "") # uma string VAZIA é false, sua negação é TRUE.
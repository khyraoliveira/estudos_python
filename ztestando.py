lista = [5, 10, 45, 2]

soma = 0
for num in lista:
    if num % 2 == 0:
        soma += num

print(soma)

def par(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(par(3))

soma = 0
for num in lista:
    if par(num):
        soma += num

print(soma)

soma = 0
for num in lista:
    if not par(num):
        soma += num

print(soma)
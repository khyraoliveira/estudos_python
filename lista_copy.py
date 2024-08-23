lista = [1, "Python", [40, 30, 20]]

lista.copy()
# ele gera uma lista igualzinha mas com uma instância diferente
# para não fazer besteira na lista original

print(lista)  # [1, "Python", [40, 30, 20]]

# Abaixo você verá que geram até IDs diferentes, porque é só uma cópia!
l2 = lista.copy()
print(id(l2), id(lista))
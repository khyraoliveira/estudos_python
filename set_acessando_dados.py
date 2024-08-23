# Conjuntos em python NÃO SUPORTAM indexação e nem fatiamento!
# caso queira acessar os seus valores é necessário CONVERTER o conjunto para lista!

numeros = {1, 2, 3, 2} # esse é o conjunto

numeros = list(numeros) # converte para uma lista

print(numeros[0]) # agora consegue acessá-los!
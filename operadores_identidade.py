# São operadores utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.print

curso = "Curso de Python"
nome_curso = curso # então aqui também tem o valor "Curso de Python"
saldo, limite = 200, 200 # ambas recebem o valor '200'

print(curso is nome_curso)
print(curso is not nome_curso)
print(saldo is limite)
# O WHILE é usado para repetir um bloco de código várias vezes.
# Faz sentido usar o WHILE quando não sabemos o número exato de vezes que
# nosso bloco de código será executado

opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

# o IF executa, mas só uma vez.
# o WHILE vai executar toda vez que a condição for atendida.
# pode colocar um ELSE no final, se quiser
# else:
#    print("Obrigado por usar o nosso sistema bancário!")
# pode usar um BREAK no final também
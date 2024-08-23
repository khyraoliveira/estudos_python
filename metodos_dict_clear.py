# { }.clear
# coloca a variável do dict .clear
# daí APAGA TODOS os valores do dicionário

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "mariana@gmail.com": {"nome": "Mariana", "telefone": "3344-9871"},
    "caio@gmail.com": {"nome": "Caio", "telefone": "3344-7766"},
}

contatos.clear()
contatos # {}
def criando_poema(data_criacao, *list, **dictionary):
    texto = "\n".join(list)
    kwargs = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dictionary.items()])
    msg = f"{data_criacao}\n\n{texto}\n\n{kwargs}"
    print(msg)
criando_poema(
    "25 de Agosto de 2024",
    "O Peido", "O peido é um som sonoro", "Da cidade do intestino", "Avisando ao chefe bunda", "Que o trem bosta já vem vindo",
    Autor="Desconhecido", Ano="1998")
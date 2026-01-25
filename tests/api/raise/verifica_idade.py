def verifica_idade(idade):
    if idade < 18:
        raise ValueError("Acesso negado para menores de idade")
    return "Acesso Permitido"
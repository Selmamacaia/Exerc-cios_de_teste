def criar_baralho():
    naipes = ['o', 'c', 'e', 'p']
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    baralho = [(valor + naipe) for naipe in naipes for valor in valores]
    return baralho

# Exemplo de uso:
baralho_completo = criar_baralho()
print(baralho_completo)

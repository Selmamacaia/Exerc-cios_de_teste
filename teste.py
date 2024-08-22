def naipe_de_cartas(naipe):
    cartas = []
    for i in range(2, 11):
        cartas.append(str(i) + naipe) 
    cartas.append('J' + naipe)  
    cartas.append('Q' + naipe) 
    cartas.append('K' + naipe)  
    cartas.append('' + naipe)  
    return cartas


naipe_copas = str(input('digite a letras: '))
cartas_copas = naipe_de_cartas(naipe_copas)
print(cartas_copas)  # ['1c', '2c', '3c', ..., '10c', 'Jc', 'Qc', 'Kc']

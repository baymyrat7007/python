dictionary = {
    'alma':{'bahasy':15,'mukdary': 30},
    'mandarin':{'bahasy':30,'mukdary': 10},
    'kivi' : {'bahasy':18,'mukdary': 1},
    'banan': {'bahasy':27,'mukdary': 20},
    'nar': {'bahasy':18,'mukdary': 15}
}
summa = []
while True:
    haryt = input('Name almak isleyarsiniz? ').lower()
    if haryt in dictionary:
        massa = int(input('Nace kg almak isleyarsiniz? '))
        x =dictionary[haryt]['bahasy'] * massa
        summa.append(x) 
    elif haryt == 'quit':
        break
    else:
        print(f"{haryt.capitalize()} dukanda yok")
print('Siz',sum(summa),'manat tolemeli')
def okuvcy_gos(ady,kursy,bahasy):
    with open ("okuwcy_maglumat.txt", 'a') as fayl:
        fayl.write(f"{ady},{kursy},{bahasy}\n")

def okuvcy_gorkez():
    with open ("")
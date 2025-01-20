def dictionary_menu():
    print("* * * * * KITAPHANA * * * * *")
    print("1. Kitaplary gormek")
    print("2. Kitap almak")
    print("3. Kitap tabsyrmak")
    print("4. Cykmak")

def kitaplary_gormek():
    kitaplar = {
        101:{'ady': 'Permanyn ', 'awtory': 'A.Govshudov', 'sany':8},
        102:{'ady': 'Saylanan eserler ', 'awtory': 'G.Ezizow', 'sany':12},
        103:{'ady': 'Ykbaly', 'awtory': 'H.Deryayew', 'sany':6},
        104:{'ady': 'Leyli Mejnun', 'awtory': 'N.Andalyp', 'sany':4},
        105:{'ady': 'Oylanma bayry', 'awtory': 'K.Gurbannepesow', 'sany':9},
    }
    for key, value in kitaplar.items():
        print(f"{key} - {{'ady':'{value['ady']}', 'awtory': '{value['awtory']}', 'sany': {value['sany']} }} ")
def kitap_almak():
    kitap_belgisi = int(input("Kitap belgisi: "))
    kitap_sany = int(input("Kitap sany: "))
    print(f"Siz H.Deryayew - yn Ykbal kitabyndan {kitap_sany} sany aldynyz!") 

def kitap_tabsyrmak():
    kitap_belgisi = int(input("Kitap belgisi: "))
    kitap_sany = int(input("Kitap sany: "))
    print(f"Siz N.Andalyn - yn Leyli Mejnun kitabyndan  {kitap_sany} sany tabsyrdynyz!") 

def main():
    while True:
        dictionary_menu()
        saylan = int(input("Saylan:  "))
        if saylan == 1: 
            kitaplary_gormek()
        elif saylan == 2:
            kitap_almak()
        elif saylan == 3:
            kitap_tabsyrmak()
        elif saylan == 4:
            print("Sag bolun, Kitaphana gelip durun! ")
            break
        else:
            print("Nadogry buyruk")
main()            



    
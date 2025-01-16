# Soraglar we dogry jogaplar bilen bir sanaw
soraglar = [
    ("Fransiýanyň paýtagty näme?", ["London", "Paris", "Berlin", "Madrid"], "Paris"),
    ("'Harry Potter' kitabyň awtory kim?", ["J.K. Rowling", "Stephen King", "George R.R. Martin", "J.R.R. Tolkien"], "J.K. Rowling"),
    ("Ýerden iň uzakda ýerleşýän planet näme?", ["Merkuriý", "Ýupiter", "Saturn", "Neptun"], "Neptun"),
    ("2018 FIFA Dünýä Kubogyny haýsy ýurt gazandy?", ["Braziliýa", "Germaniýa", "Fransiýa", "Argentina"], "Fransiýa"),
    ("Monalisany kim döretdi?", ["Leonardo da Winçi", "Pablo Pikasso", "Winsent van Gog", "Mikelanjelo"], "Leonardo da Winçi"),
    ("Haysy gahryman 'Corekci kocesinde' yasayar?", ["Superman", "Komisar Merge", "Şerlok Holms", "Jeýms Bond"], "Şerlok Holms"),
    ("Gyzyl planet hökmünde tanalýan planet näme?", ["Mars", "Ýupiter", "Saturn", "Neptun"], "Mars"),
    ("Bil Geýts haýsy kompaniýanyň düýbüni tutujy hasaplanýar?", ["IBM", "Apple", "Microsoft", "Acer"], "Microsoft"),
    ("Haýsy kofeniň bir görnüşi däldir?", ["Moka", "Latte", "Makiato", "Pesto"], "Pesto"),
    ("Afrikanyň iň uzyn derýasy haýsy?", ["Nil", "Kongo", "Zambezi", "Limpopo"], "Nil")
]

# Başlangyç baly
bal = 0
dogry_jogap_sany = 0
yalnys_jogap_sany = 0
sorag_sany = 0  # Soraglaryň sanyny hasaplamak üçin

# 10 sorag sorandan soň oýuny tamamlap, netije görkezýän döngü
for sorag in soraglar:
    # Soraglary görkezeris
    print(f"Sorag: {sorag[0]}")
    jogaplar = sorag[1]  # Jogaplar sanawy
    dogry_jogap = sorag[2]  # Dogry jogap

    # Jogaplary görkezýäris (1-den başlaýan nomerler bilen)
    print(f"1. {jogaplar[0]}")
    print(f"2. {jogaplar[1]}")
    print(f"3. {jogaplar[2]}")
    print(f"4. {jogaplar[3]}")

    # Ulanyjynyň jogabyny alýarys
    ulanyjy_jogaby = int(input("Jogabyňyzy saýlaň (1-4): ")) - 1

    # Jogabynyň dogrylygyny barlaýarys
    if jogaplar[ulanyjy_jogaby] == dogry_jogap:
        print("Dogry jogap!")
        bal += 10  # Dogry jogap üçin 10 bal goşýarys
        dogry_jogap_sany += 1
    else:
        print(f"Ýalňyş jogap! Dogry jogap: {dogry_jogap}")
        bal -= 5  # Ýalňyş jogap üçin 5 bal aýyrýarys
        yalnys_jogap_sany += 1

    sorag_sany += 1  # Soraglaryň sanyny hasaplaýarys
    
    # Eger 10 sorag soralan bolsa döngini bozýarys
    if sorag_sany == 10:
        break

    print()  # Bir setir boş ýer goýýarys

# Oýnuň soňunda jemleýji netije
print("")
print(f"Oýun tamamlandy! 🎉🎊🎈🎇🎆✨✨🎉 \nJemi bal: {bal}")
print(f"Dogry jogaplaryň sany: {dogry_jogap_sany}")
print(f"Ýalňyş jogaplaryň sany: {yalnys_jogap_sany}")

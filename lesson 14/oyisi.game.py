soraglar = [
    {"sorag": "Turkiyen paytagty haysy saherdir?",
    "Jogaplar":["Istanbul", "Ankara", "Izmir", "Antalya"],"dogry": 1},
    {"sorag": "Python dili nadip tanalyar?", 
    "Jogaplar": ["Ozlesdirilyan dil", "Caklendirilyan dil", "Yonekey dil", "Obyekt dil"], "dogry": 0},
    {"sorag": "TGT hytayyn paytagty haysy saherdir?",
    "Jogaplar": ["Sanxay", "Pekin", "Hong Kong", "Macau"],"dogry": 1},
    {"sorag": "Geografiya ylmy kim tarapyndan doreldildi?",
    "Jogaplar": ["Eyfel", "Aristotel", "Eratosthenes", "Galilei"], "dogry": 2},
    {"sorag": "Turkmenistanyn hazirki prezidenti kim?", 
    "Jogaplar": ["Berdimuhammedow", "Serdar Berdimuhamedow", "Saparmyrat Nyyazow", "Gurbanguly Berdimuhammedow"], "dogry": 1}
    {"sorag" : "Halkara Olimpiya komitetinin baslygy kim?",
    "Jogaplar": ["Thomas Bach", "Juan Antonio Samaranch", "Pierre de Coubertin", "Sebastian Coe"],"dogry":0},
    {"sorag": "Turkmenistanda in uly derya haysy?",
    "Jogaplar": ["Amyderya", "Murgap", "Tejen"], "dogry": 0},
    {"sorag": "In uzyn deniz haysy?", 
    "Jogaplar": ["Yaponiya denzi", "Hindi okeany", "Atlantik okeany", "Bering denzi "], "dogry": 2},
    {"sorag": "Nebula name?", 
    "Jogaplar": ["Astronomik obyekt", "Kainatdaki agyr jisim", "Kate astronomik galaktika", "Basga planetanyn atmosferasy"],"dogry": 0},
    {"sorag": "Turkmenistanyn dowlet baydagynyn renki namelerden ybarat?", 
    "Jogaplar": ["Yasyl we ak", "Gyzyl we ak", "gok we ak", "Yasyl we gok"],"dogry": 1}
]
bal = 0
dogry = 0
yalnys = 0
for sorag in soraglar:
     print(f"\n{sorag['sorag']}")
     for idx, jogap in enumerate(sorag['jogaplar']):
         print(f"{idx + 1}. {jogap}")
    jogap_index = int(input("Jogabynyzy saylan (1-4): ")) -1
    if jogap_index == sorag ["dogry"]:
        bal += 10
        dogry += 1
        print("Dogry jogap!")
    else:
        bal -= 5
        dogry += 1
        print("Yalnys jogap!")
print(f"\nOyunyn ahyrynda:")
print(f"Dogry jogaplar:{dogry}")
print(f"Yalnys jogaplar: {yalnys}")
print(f"Jemleyji bal:{bal}")

]
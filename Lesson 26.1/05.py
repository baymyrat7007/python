import datetime 
def yazgy_gos():
    yazgy = input("To Do List? \n")
    senesi = datetime.datetime.now().strftime("%Y - %m - %d %H:%M:%5")
    with open("ToDoLIst.txt", 'a') as fayl:
        fayl.write(f"{senesi} - {yazgy}\n ")
    print("yazgy gosuldy")

def yazgylary_gorkez():
    with open("To Do LIst.txt", "r") as fayl:
        setirler = fayl.readlines()

    if not setirler:
        print("Gunlik yazgy yok")

    else:
        print("Gunlik yazgylary: ")
        for setir in setirler:
            print(setir)

print("Gunlik ulgamy")
while True:
    bolum = input("\nTaze yazgy gosmak (1) ya-da Gunlik yazgylary gormek (2), Cykmak (3)")
    if bolum == "1":
        yazgy_gos()
    elif bolum == "2":
        yazgylary_gorkez()
    elif bolum == "3":
        print("Programmany ulananynyz un sag bolun")
        break



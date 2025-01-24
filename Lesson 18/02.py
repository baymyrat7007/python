def user_name(dogry_ulanyjy, dogry_parol, maks_ymtylma):
    ymtylma_sany = 0

    while ymtylma_sany < maks_ymtylma:
        ulanyjy_ady = input("Ulanyjy adyny girizin: ")
        parol = input("Parol girizin: ")

        if ulanyjy_ady == dogry_ulanyjy and parol == dogry_parol:
            print("Hos geldiniz!")
            
        else:
            ymtylma_sany += 1
            print("Ulanyjy ady yada parol nadogry")

    if ymtylma_sany == maks_ymtylma:
        print("Hasaba girmage bolan mumkinciliginiz gutardy. ")

user_name("user123", "parol456", 3)



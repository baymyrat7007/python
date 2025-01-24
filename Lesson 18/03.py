def bir_san():
    kop = 1
    if san >= 0:
        for i in range(1, san + 1):
            kop*=1
        return kop
    else:
        print("yalnys san") 

user = int(input("Bir sany girizin: "))
print("Faktoriyal: ", bir_san())
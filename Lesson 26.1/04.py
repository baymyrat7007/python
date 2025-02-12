with open("Sanlar.txt", "r") as fayl:
    A = fayl.read().split()

    B = []
    for i in A:
        B.append(int(i))

    C = []
    D = []
    for i in B:
        if i > 0:
            C.append(i)
        else:
            D.append(i)

with open ("Polozitel.txt", "w") as fayl:
    for i in C:
        fayl.write(str(i) + "\t")

with open ("Otrisatel.txt", "w") as fayl:
    for i in D:
        fayl.write(str(i) + "\t4")
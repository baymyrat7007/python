with open("Sanlar.txt", "r") as file:
    A = file.read().split()
    B = []
    for i in A:
        B.append(int(i))

with open("Sanlar2.txt", "w") as file:
    file.write(f"IN uly san :{max(B)}\n")
    file.write(f"IN kici san :{min(B)}\n")
    file.write(f"Jemi:{sum(B)}\n")
    file.write(f"Ortaca baha: {sum(B)/len(B)}\n")
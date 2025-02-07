okuvcylar = {"Nurberdi": 17,
             "Batyr": 15,
             "Selim": 12
}

print(okuvcylar)

okuvcylar["Nurberdi"] = 18
print(okuvcylar)

okuvcylar.pop("Selim")
print(okuvcylar)

for i in okuvcylar:
    print(okuvcylar[i])
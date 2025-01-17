dictionary = {"Anna": {"synag1": "98",
                       "synag2": "100",
                       "synag3": "100"},
            "Merdan": {"synag1": "85",
                     "synag2": "90",
                     "synag3": "0"},
            "Oraz":{"synag1": "50",
                    "synag2": "70",
                    "synag3": "80"},
}
ady = input("Ady: ")
if ady in dictionary:
    isleg = input("Ahli synaglar:(howa/yok)")
    if isleg == "howa":
        print(dictionary[ady])
    else:
        mag =input("synag1/synag2/synag3: ")
        print(dictionary[ady][mag])
else:
    print(f"{ady} synag bahalary")
with open ("Students.txt", "w") as baymyrat:
    for i in range (1,6):
        ady = input(f"{i} - ady: ")
        baymyrat.write(f"{i} - {ady}\n")
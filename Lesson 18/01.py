def gosmak():
    print(f"Netije: {float(san1 + san2)}")


def ayyrmak():
    print(f"Netije: {float(san1 - san2)}")

def kopeltmek():
    print(F"Netije: {float(san1 * san2)}")

def bolmek():
    print(f"Netije: {float(san1 / san2)}")

def cykys():
    print("Cykys")



while True:
    san1 = int(input("Birinji sany girizin: "))
    san2 = int(input("Ikinji sany girizin: "))
    funksiya = input("Funksiya saylan: +, -, *, /\nFunksiya: ")
    if funksiya == "+":
        gosmak()
    elif funksiya == "-":
        ayyrmak()
    elif funksiya == "*":
        kopeltmek()
    elif funksiya == "/":
        if san2 != 0:
            bolmek()
        else:
            print("San bolunenok")
    elif funksiya == "quit":
        cykys()
        break
        
def numbers():
    numbers_1 = []
    while True:
        num = int(input("Bir san girizin ( Durmak ucin 0 ): "))
        if num == 0:
            break
        numbers_1.append(num)
    if len(numbers_1) == 0:
        print("Hic san girizilmedi.  ")
    elif len (numbers_1) == 1:
        print(f"Dine bir san girizildi. In uly hem in kici san: {numbers_1[0]}")
    else:
        print(f"In uly san: {max(numbers_1)}, IN kici san: {min(numbers_1)}")

numbers()
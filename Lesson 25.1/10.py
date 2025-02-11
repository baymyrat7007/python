with open ("Students.txt", "r") as file:
    content  = file.read().split()
    numbers = list(map(int, content.split())) if content else[]

if numbers:
    max_num = max(numbers)
    min_num = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    with open ("Sanlar2.txt", "w") as file:
        file.write(f"In uly san: {max_num}\n")
        file.write(f"In kici san: {min_num}\n")
        file.write(f"Jemi: {total}\n")
        file.write(f"Ortaca baha:{average:.1f} \n")
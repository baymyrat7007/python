with open ("Students.txt", "r") as file:
    content = file.read(). strip()
    nubers = list (map(int, content.split())) if content else []
    
positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]

with open ("Polozitel.txt", "w") as file:
    file.write(" ".join(map(str, posotive_numbers )))

with open ("Otrisatel.txt", "w") as file:
    file.write(" ".join(map(str, negative_numbers)))
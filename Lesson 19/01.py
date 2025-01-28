def education():
    print("Welcome to the Education System")
    student = {}
    while True:
        name = input("Enter the student name (done): ").strip()
        if name.lower() == "done":
            break

        grade_input = input(f"Enter {name} is grade: ").strip()
        if grade_input.isdigit():
            grade =int(grade_input)
            student[name] = grade
        else:
            print("Please enter a vaild number for the grade.")

    total_grade = 0
    for name, grade in student.items():
        total_grade += grade
        if grade >= 90:
            print(f"{name} has an A. Exellent work!")
        elif grade >= 80:
            print(f"{name} has a B. Good job!")
        else:
            print(f"{name} has failed. Additional support needed.")

    if student:
        class_average = total_grade / len(student)
        print(f"\nClass average: {class_average:.2f}")
    else:
        print("No students were entered. ")
education()

        
def okuwcy_hasapla(student_count):
    passed_count = 0
    total = 0

    for i in range(student_count):
        print = int(input(f'{i+1}. okuwcy bally: '))

        if point >= 50:
            passed_count +=1
        
        total += point

    gecenler = passed_count
    gecmedikler = student_count - passed_count
    ortaca = total // student_count

    print(f'Gecenler:{gecenler}')
    print(f'Gecmedikler:{gecmedikler}')
    print(f'Ortaca bal:{ortaca}')

student_count = int(input('Okuwcylaryn sany:'))
okuwcy_hasapla(student_count)

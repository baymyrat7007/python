numbers = [1,2,3,4,5,6]
jubut_sanlar = [num for num in numbers if num % 2 == 0]
tak_sanlar = [num for num in numbers if num % 2 != 0]

print("Jubut sanlar:", jubut_sanlar)
print("tak_sanlar:", tak_sanlar)
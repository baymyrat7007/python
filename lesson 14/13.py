numbers = [1, 2, 3, 1, 2, 1]
num_1 = [num for num in numbers if numbers.count(num) == 1]
if len (num_1) == 1:
    print(num_1[0])
else:
    print(" no number")
    
        
print(""" 
Jemi 10 sorag 
""")

import random 
jemi1 = 0
jemi2 = 0
for i in range (1,11):
    a = random.randint(1,30)
    b = random.randint(1,30)
    print(f"{i} - nji sorag\n {a} + {b} = ?")
    jogap = int(input("Your answer:  "))
    if jogap == a + b:
        print("correct")
        jemi1 += 1

    elif jogap != a + b:
        print(f"Your answer is incorrect! Correct answer is {a + b}")


print("***** YOUR result *****")
print("QUESTION: 10")
print(f"Correct answer: {jemi1}")
print(f"Incorrect answer: {jemi2} ")
print(f"{jemi1 * 100 / 10}%")
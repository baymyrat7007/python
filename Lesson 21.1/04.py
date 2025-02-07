import random 
o = ["Picture", "Number"]
n = 0
p = 0 
for  i in range(1,11):
    number = random.choice(0)
    if number == "Number":
        n += 1
    else:
        p += 1
    print(f"{i} {number}")

print(f"Number: {n}")
print(f"Picture: {p}")

if n > p:
    print("Kop cykan NUmber")

elif n < p:
    print("Kop cykan Picture")
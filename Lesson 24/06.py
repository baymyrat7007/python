import datetime
print("Enter date in the past: ")
y = int(input("Year:"))
m = int(input("Month: "))
d = int(input("Day: "))
T = datetime.datetime.today()
F = datetime.datetime(y,m,d)
R = T - F
print(R.days, "days have passed")
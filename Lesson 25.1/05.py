import datetime
time = datetime.datetime.today()
duyun = datetime.timedelta(days = 1)
d = time - duyun
t = time + duyun


with open("Kompyuter.txt", "w") as fayl:
    fayl.write(d.strftime("%d.%m.%y\t" "%A\n"))
    fayl.write(time.strftime("%d.%m.%y\t" "%A\n"))
    fayl.write(t.strftime("%d.%m.%y\t" "%A\n"))


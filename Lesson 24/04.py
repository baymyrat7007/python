import datetime
wagt = datetime.datetime(2005,2,22,8,30,00)

print("Doglan senam: ", wagt)
print(wagt.strftime("Hepdanin %w-nji gununde doguldym "))
print(wagt.strftime("Shol gun yylyn %j- gunidi"))
print(wagt.strftime("shol hepde yylyn %U- hepdesi"))
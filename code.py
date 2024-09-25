import datetime


d1 = datetime.datetime.strptime(input(), '%d %b %Y').date()
d2 = datetime.datetime.strptime(input(), '%d %b %Y').date()
sat = (d2 - d1).days // 7
sun = sat
if 6 - d1.weekday() <= (d2 - d1).days % 7:
    sun += 1
if (12 - d1.weekday()) % 7 <= (d2 - d1).days % 7:
    sat += 1
print('Saturday:', sat)
print('Sunday:', sun)

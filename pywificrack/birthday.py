f = open('birthday.txt','w')
for yr in range(1980,2000):
    for mon in (1,13):
        for day in (1,32):
            data = str(yr)
            if mon < 10:
                data = data + '0' + str(mon)
            else:
                data = data + str(mon)
            if day < 10:
                data = data + '0' + str(day)
            else:
                data = data + str(day)
            f.write(data + '\n')
f.close()

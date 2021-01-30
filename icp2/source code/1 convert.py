Nstudents = int(input('How many students? '))
listNheightinfeet = []
listNheightincm = []

# 30.48
temp = 0
for studentHieght in range(int(Nstudents)):

    temp = float(input("Hieght of student {} ".format(studentHieght + 1)))
    listNheightinfeet.append(temp)


listNheightincm = [int(i * 30.48) for i in listNheightinfeet]


print("Hieght in feet : ", listNheightinfeet)

print("Hieght in cm: ", listNheightincm)



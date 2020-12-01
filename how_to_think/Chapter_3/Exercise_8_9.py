opposite = (float(input("enter length of side 1 in cm:")))**2

adjacent = (float(input("enter length of side 2 in cm:")))**2

hypotenuse = (float(input("enter length of side 3 in cm:")))**2


threshold = 1**(-7)

if abs((opposite+adjacent)-hypotenuse) < threshold or abs((hypotenuse+adjacent)-opposite) < threshold or abs((opposite+hypotenuse)-adjacent) < threshold:
    print(True)

else:
    print(False)


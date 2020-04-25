import math

a = float(input("Enter (a) value here: "))
b = float(input("Enter (b) value here: "))
c = float(input("Enter (c) value here: "))

discr = b ** 2 - 4 * a * c

if discr < 0:
    print("There are no real roots")
    print("There are no solutions")
elif discr == 0:
    print("There is one real root")
    value1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The solution is: " + str(value1))
elif discr > 0:
    print("There are two real roots")
    value1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    value2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print("The solutions are: " + str(value1) + " and " + str(value2))
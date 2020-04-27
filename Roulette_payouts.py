import random
import sys

lst = []
lstred = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
lstblack = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
lst1to18 = []
lst19to36 = []

for i in range(37):
    lst.append(i)
lst.append(00)
for i in range(1, 19):
    lst1to18.append(i)
for i in range(19, 37):
    lst19to36.append(i)

num = random.choice(lst)

num = str(num)

print("The spin resulted in " + num)

num = int(num)

if num == 0:
    print("Pay 0")
    sys.exit()
elif num == 00:
    print("Pay 00")
    sys.exit()
else:
    num = str(num)
    print("Pay " + num)

num = int(num)
if num in lstred:
    print("Pay Red")
elif num in lstblack:
    print("Pay Black")
if num % 2 == 1:
    print("Pay Odd")
elif num % 2 == 0:
    print("Pay Even")
if num in lst1to18:
    print("Pay 1 to 18")
elif num in lst19to36:
    print("Pay 19 to 36")
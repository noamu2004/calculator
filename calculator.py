import math
peoola = int(input("put a peoola heshbonit, 1 hiboor, 2 hisoor, 3 kefel, 4 hilook, 5 hezka, 6 shoresh ribooee"))
if (peoola == 6):
    num1 = int(input("put first number"))
    if(num1 >= 0):
        print (math.sqrt(num1))
    else:
        print("wrong action")
else:
    num1 = int(input("put first number"))
    num2 = int(input("put second number"))
    if (peoola == 1):
        print(num1 + num2)
    elif (peoola == 2):
        print(num1 - num2)
    elif (peoola == 3):
        print(num1 * num2)
    elif ((num2 != 0) and (peoola == 4)):
        print(num1 / num2)
    elif (peoola == 5):
        print(num1 ** num2)
    else:
        print("wrong action")

import os

os.system("cls")
print("Input an integer positive number:")
ulNum = int(input())
if ulNum % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
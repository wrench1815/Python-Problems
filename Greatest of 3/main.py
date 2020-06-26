num1 = int(input('Enter Number 1: '))
num2 = int(input('Enter Number 2: '))
num3 = int(input('Enter Number 3: '))

if num1 >= num2 and num1 >= num3:
    print('Greatest of 3 is: ', num1)
elif num2 >= num1 and num2 >= num3:
    print('Greatest of 3 is: ', num2)
else:
    print('Greatest of 3 is: ', num3)

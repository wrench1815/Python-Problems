num = int(input('Enter Numerator: '))
den = int(input('Enter Denominator: '))

if num % den == 0:
    print(num, 'is divisible by', den)
else:
    print(num, 'is not divisible by', den)

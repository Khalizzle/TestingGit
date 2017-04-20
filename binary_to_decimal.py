binary = input('Enter a binary number: ')
print(binary)

dec = int(binary, 2)
if dec == ValueError:
    print('not allowed')
else:
    print(dec)

deci = 0
for digits in binary:
    deci = deci*2 + int(digits)

print(deci)

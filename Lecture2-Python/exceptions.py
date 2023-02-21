import sys

# to handle if you enter a word
try: 
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print('error: invalid input')
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("error: cant not divide by zero")
    sys.exit(1)

print(f'{x} / {y} is {result}')
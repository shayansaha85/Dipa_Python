
number1 = int(input('Enter number1 : '))
number2 = int(input('Enter number2 : '))
operator = input('Enter operator [+, -, *, /] : ')

if operator == '+':
      print(number1 + number2)
elif operator == '-':
      print(number1 - number2)
elif operator == '*':
      print(number1 * number2)
elif operator == '/':
      print(number1 / number2)
else:
      print('INAPPROPRIATE OPERATOR')

      

number1 = int(input('Enter number1 = '))
number2 = int(input('Enter number2 = '))
number3 = int(input('Enter number3 = '))


if number1 > number2 and number1 > number3:
      print(f'{number1} is the greatest one')
elif number2 > number1 and number2 > number3:
      print(f'{number2} is the greatest one')
else:
      print(f'{number3} is the greatest one')

      
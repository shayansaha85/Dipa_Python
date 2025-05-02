
number = int(input('Enter a number = '))
counter = 0

if number in [0,1]:
      print('Not appropriate')

else:
      for i in range(2, number):
            if number%i == 0:
                  counter += 1
                  
      if counter == 0:
            print('PRIME')
      else:
            print('NON-PRIME')

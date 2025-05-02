
number = int(input('Enter a number = '))

counter = 0

if number in [0,1]:
      print('Inappropraite')
else:
      i = 2
      while i<number:
            if number%i == 0:
                  counter += 1
            i=i+1
      
      if counter == 0:
            print('PRIME')
      else:
            print('NON-PRIME')
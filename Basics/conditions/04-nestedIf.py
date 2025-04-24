
country = input('Enter your country name : ')
age = int(input('Enter your age : '))

if country.upper() == 'INDIA':
      if age >= 18:
            print('You are Indian and adult. ELIGBLE')
      else:
            print('You are Indian but not adult. NOT ELIGBLE')
else:
      print('You are not Indian. NOT ELIGIBLE')
            
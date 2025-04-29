
"""
2024

4 divisble --> 100 not divisible or 400 divisble
1900 / 4
2000 / 
"""

year = int(input('Enter a year : '))

if year%4 == 0:
      if year%100 != 0 or year%400 == 0:
            print('LEAP YEAR')
      else:
            print('NOT LEAP YEAR')
else:
      print('NOT LEAP YEAR')

      
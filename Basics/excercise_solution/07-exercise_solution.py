
marks = int(input('Enter marks (out of 100 ): '))


if marks <= 100:
      if marks >= 90:
            print('Grade A')
      elif marks >=80 and marks <=89:
            print('Grade B')
      elif marks >= 70 and marks <= 79:
            print('Grade C')
      elif marks >= 60 and marks <= 69:
            print('Grade D')
      else:
            print('Grade F')
else:
      print('Invalid marks. Should be less than 100')

number = int(input('Enter a number = '))
number_backup = number
reverse_number = 0

while number_backup!=0:
      r = number_backup%10
      reverse_number = reverse_number*10 + r
      number_backup = number_backup // 10 

if number == reverse_number:
      print('Palindrome')
else:
      print('not palindrome')


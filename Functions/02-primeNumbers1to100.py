
def isPrime(number):
      count = 0
      if number in [1,0]:
            return False
      else:
            for i in range(2, number):
                  if number%i == 0:
                        count += 1
            if count == 0:
                  return True
            else:
                  return False
            
for i in range(1, 101):
      if isPrime(i):
            print(i)

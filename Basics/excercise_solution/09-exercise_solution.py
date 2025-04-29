
principal = float(input('Enter the principal : '))
interest_rate = float(input('Enter the ROI : '))
time = float(input('Enter the tenure in years : '))

interest = (principal * interest_rate * time) / 100

interest_rounded_off = round(interest, 2)

print(interest_rounded_off)


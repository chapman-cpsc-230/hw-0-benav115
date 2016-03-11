year = 1900

if year%400 == 0 or (year%4 == 0 and year%100 != 0): # != means does not equal and % means divide
    print year,"is a leap year"
else:
    print year,"is not a leap year"

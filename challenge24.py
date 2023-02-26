'''Write a function is_leap_year() that determines 
whether a year is a leap year.A leap year is 
divisible by 4, but not by 100.It is also divisible by 400.'''

def is_leap_year(year:int):
    if year % 4 == 0:
        print (f'{year} is a leap year')
    elif year % 4 != 0:
        print (f'{year} is not a leap year')   

is_leap_year(2023)



def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print '%d is leap year!' % year
    else:
        print '%d is not leap year!' % year
    return 0


print leapyear(2013)
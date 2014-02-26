def add ( a , b ):
	print '%d + %d = ' % (a , b)
	return a + b
def subtraction (a , b ):
	print '%d - %d = ' %( a , b)
	return a - b
def multiplication (a , b):
	print '%d * %d = ' %( a , b )
	return a * b
def division (a , b):
	print '%d / %d = ' % (a , b)
	return a / b
a = 24
b = 34
c = 100
d = 1023

what = add(a , subtraction(division(b , c) , d))
print "24 + 34 / 100 - 1023 = %d" % what

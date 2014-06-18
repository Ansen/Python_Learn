'readTextFile.py  -- read and display text file'

fname = raw_input('Enter Filename: ')
print

try:
    fobj = open(fname, 'r')
except IOError, e:
    print "*** file open error: ", e
else:
    for eachline in fobj:
        print eachline,
    fobj.close()

'readNwriteTextFiles.py -- create and read text file'
import os

def CreateTextFile():
    while True:
        fname = raw_input('Enter Filenane: ')
        if os.path.exists(fname):
            print "ERROR: '%s' already exists" % fname
        else:
            break
    all = []
    print "\nEnter lines ('.' by itself to quit).\n"
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            all.append(entry)
    ls = os.linesep
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in all])
    fobj.close()
    print 'DONE!'

def ReadTextFile():
    fname = raw_input('Enter Filename: ')
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print "*** file open error: ", e
    else:
        for eachline in fobj:
            print eachline,
    fobj.close()


print """If you want to create text file, enter '1'.
         If you want to read text file, enter '2'."""
Choice = raw_input('> ')


if Choice == '1':
    CreateTextFile()
elif Choice == '2':
    ReadTextFile()
else:
    print 'Input Error!'
    


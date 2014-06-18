import os
import sys

def ReadTextFile(fname):
    try:
        fobj = open(fname, 'r')
    except IOError, e:
        print '*** file open error: ', e
    else:
        items = []
        num = 0
        for x in fobj:
            x = x.rstrip('\n')
            x = x.rstrip('\r')
            print '%s %s'%(num, x)
            items.append(x)
            num +=1
    fobj.close()
    return items

def WriteTextFile(fname, items):
    fobj = open(fname, 'w')
    fobj.writelines(['%s%s' %(x,ls) for x in items])
    fobj.close()

def CreateNewTextFile(fname):
    items = []
    print "\nEnter lines ('.' by itself to quit).\n"
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            items.append(entry)
    WriteTextFile(fname,items)
    print '%s was created.' %fname

def EditTextFile(fname):
    items = ReadTextFile(fname)
    print '\nEnter num to EDIT  a to ADD a line'
    Edit_or_Add = raw_input('> ')
    
    if Edit_or_Add == 'a':
        a = raw_input('Enter your words\n> ')
        items.append(a)
        
    elif Edit_or_Add <= len(items):
        a = raw_input('Enter your new words\n> ')
        items[int(Edit_or_Add)] = a
        
    else:
        print "I dont't know '%s', Bye!" %Edit_or_Add
        sys.exit()

    save = raw_input('Enter y to save other words to quit and not save:')
    if save == 'y':
        WriteTextFile(fname, items)


print """
         Enter a filename,you can do three things:
         1.Create an new text file if it not exists.
         2.Edit text file .
         3.View the contents of a file.
        """
ls = os.linesep
fname = raw_input('Now,Enter a Filename: ')
if os.path.exists(fname):
    print "'%s' already exists" % fname
    print """
        Enter 1 to view, 2 to edit, other words to exit
        """
    edit_or_view = raw_input("> ")
    if edit_or_view == '1':
        ReadTextFile(fname)
    elif edit_or_view == '2':
        EditTextFile(fname)
else:
    print "'%s' does not exists, create a new" % fname
    CreateNewTextFile(fname)
print 'Bye!'
    
    

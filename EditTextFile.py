'EditTextFile.py -- Edit text file line by line'
import os

def CreateNewTextFile(Cname):
    Contents = []
    print "\nEnter lines ('.' by itself to quit).\n"
    while True:
        entry = raw_input('> ')
        if entry == '.':
            break
        else:
            Contents.append(entry)
    fobj = open(Cname, 'w')
    fobj.writelines(['%s%s' % (x, ls) for x in Contents])
    fobj.close()
    print '%s was created.' %Cname
    print Contents

def EditTextFile(Ename):
    fobj = open(Ename, 'r')
    tmp = []
    i = 0
    for eachline in fobj:
        i+=1
        eachline = eachline.rstrip('\n')
        eachline = eachline.rstrip('\r')
        print '%s %s'%(i, eachline)
        tmp.append(eachline)
    fobj.close()
    print '\n Enter num to EDIT  a to ADD a line'
    Edit_or_Add = raw_input('> ')
    if Edit_or_Add == 'a':
        a = raw_input('Enter your words\n> ')
        tmp.append(a)
    elif Edit_or_Add in range(0,i,1):
        e = raw_input('Enter your new words\n> ')
        tmp[int(Edit_or_Add)] = e
    else:
        exit

    save = raw_input('Enter YES to save other words to quit and not save:')
    if save == 'YES':
        Efobj = open(Ename, 'w')
        Efobj.writelines(['%s%s' %(x, ls) for x in tmp])
        Efobj.close()
def ReadTextFile(Rname):
    try:
        fobj = open(Rname, 'r')
    except IOError, e:
        print '*** file open error: ', e
    else:
        print 'FileName: ', Rname
        print 'Content:'
        for eachline in fobj:
            print eachline,
        print '\n------EOF-------'

def ChekTextFile(Chkname):
    if os.path.exists(Chkname):
        print "'%s' already exists" % Chkname
        print """
            Enter 1 to view, 2 to edit, other words to exit
            """
        edit_or_view = raw_input("> ")
        if edit_or_view == '1':
            ReadTextFile(Chkname)
        elif edit_or_view == '2':
            EditTextFile(Chkname)
    else:
        print "'%s' does not exists, create a new" % Chkname
        CreateNewTextFile(Chkname)
            
    
print """
         Enter a filename,you can do three things:
         1.Create an new text file if it not exists.
         2.Edit text file .
         3.View the contents of a file.
        """
ls = os.linesep
fname = raw_input('Now,Enter a Filename: ')
ChekTextFile(fname)
print 'Bye!'

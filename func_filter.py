def func(a):
    if a > 100:
        return True
    else:
        return False

print filter(func, [10,56,101,500])

print reduce((lambda x,y: x+y),[1,2,4,7,9])
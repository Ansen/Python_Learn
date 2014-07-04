class Bird(object):
    feather = True


class chicken(Bird):
    fly = False

    def __init__(self, age):
        self.age = age


summer = chicken(2)

print (Bird.__dict__)
print (chicken.__dict__)
print (summer.__dict__)
from oppdemo import Bird


class happyBird(Bird):
    def __init__(self, more_words):
        print 'We are happy birds.', more_words


summer = happyBird('Happy,Happy!')
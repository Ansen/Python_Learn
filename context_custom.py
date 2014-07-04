class VOW(object):
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        self.text = "I say:" + self.text
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.text = self.text + "!"


with VOW("I'm fine") as myvow:
    print (myvow.text)
print(myvow.text)
class Phone:
    def __init__(self):
        print("I am in Phone class ")


class Xiaomi(Phone):
    def __init__(self):

        print("I am in xiaomi class")
        super().__init__()


obj = Xiaomi()

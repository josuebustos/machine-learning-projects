class Person:
    """Doc - Inside Class"""

    def __init__(self, name):
        """Doc - __init__ Constructor"""
        self.n_name = name
        # print(self.n_name)

    def show(self, n1, n2):
        """Doc - Inside Show"""
       
        print("Sum = {}".format((n1 + n2)))
        return (n1 + n2)

    def __del__(self):
        print("Destructor Deleting object - {}".format(self.n_name))


p = Person("test")
p.show(2, 3)
# print(p.__doc__)
# print(p.__init__.__doc__)
# print(p.show.__doc__)

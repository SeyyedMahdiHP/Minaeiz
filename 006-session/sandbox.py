"""
    Note:
        id, title, tags, ...
    Notebook:
        Note, Note, Note, ...
    Menu:
        run(), display(), ...
"""


class User:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    @staticmethod
    def display():
        print('ye chizi')


u1 = User('ali@kalan.ir', '123456')
u2 = User('kalan@ali.ir', '7654321')
u1.display()
u2.display()



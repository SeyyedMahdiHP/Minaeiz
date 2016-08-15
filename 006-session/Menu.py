import sys
from Notebook import last_id, Notebook


# class Vector:
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __bool__(self):
#         return any((self.x, self.y, self.z))
#
#     def __len__(self):
#         return 10
#
#     def __add__(self, other):
#         pass
#
# v = Vector(0, 0, 0)
# if v:
#     print("BOOD")
#
# print(len(v))


class Menu:

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            1: self.add,
            2: self.show,
            3: self.edit,
            4: self.search,
            5: self.exit
        }

    @staticmethod
    def display():
        print("""
1 - Add a new Note
2 - Show All Notes
3 - Edit a Note
4 - Search by title
5 - Exit""")

    def run(self):
        while True:
            self.display()
            choose = int(input("Choose an option: "))
            action = self.choices.get(choose)
            if action:
                action()

    def add(self):
        title = input("Enter Your title: ")
        tags = input("Enter your tags: ")
        self.notebook.add(title, tags)

    def show(self):
        for note in self.notebook.notes:
            print("title: {0} | tags: {1}".format(note.title, note.tags))

    def edit(self):
        note_id = int(input("Enter an id: "))
        title = input("Enter a new title: ")
        if title:
            self.notebook.edit_title(note_id, title)
        tags = input("Enter new tags: ")
        self.notebook.edit_tags(note_id, tags)

    def search(self):
        query = input("Enter your query: ")
        notes = self.notebook.search(query)
        for note in notes:
            print("id: {0} | title: {1} | tags: {2}".format(note.id, note.title, note.tags))

    @staticmethod
    def exit():
        sys.exit(0)


# if __name__ == '__main__':
#     Menu().run()
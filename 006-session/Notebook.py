last_id = 0


class Note:

    def __init__(self, title, tags):
        self.title = title
        self.tags = tags
        self.id = last_id + 1

    def search(self, query):
        if self.title == query:
            return True


class Notebook:

    def __init__(self):
        self.notes = []

    def _find(self, note_id):
        for note in self.notes:
            if note_id == note.id:
                return note

    def add(self, title, tags):
        note = Note(title, tags)
        self.notes.append(note)

    def edit_title(self, note_id, title):
        note = self._find(note_id)
        if note:
            note.title = title

    def edit_tags(self, note_id, tags):
        note = self._find(note_id)
        if note:
            note.tags = tags

    def search(self, query):
        return [note for note in self.notes if note.search(query)]
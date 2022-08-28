class Book:
    def __init__(self, title, authors):
        self.title = title
        self.authors = authors

    def __hash__(self):
        return (self.title + ''.join(self.authors)).__hash__()
    def __eq__(self, o):
        return self.title == o.title and set(self.authors) == set(o.authors)

    def format(self):
        return '{title} - {authors}'.format(title=self.title, authors='; '.join(self.authors))
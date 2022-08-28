from datetime import datetime

class Highlight:
    def __init__(self, book, page, date, text):
        self.book = book
        self.page = page
        self.date = date
        self.text = text

    def format(self):
        return '{date} - Page {page}\n\n{text}\n'.format(
                    date=self.date.strftime("%d/%m/%Y %H:%M:%S"),
                    page=self.page,
                    text=self.text
                )
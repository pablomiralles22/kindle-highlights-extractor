import re
from datetime import datetime
from models.book import Book
from models.highlight import Highlight

EXPR = r'(.+) \((.+)\)\r*\n- Your Highlight (?:at|on) page ([0-9]+) \| [lL]ocation ([0-9]+)-([0-9]+) \| Added on (?:[a-zA-Z]+), ((?:[a-zA-Z]+|[0-9]+) (?:[0-9]+|[a-zA-Z]+),? (?:[0-9]{4}) (?:[0-9]+):(?:[0-9]+):(?:[0-9]+\s? ?A?P?M?))\r*\n\r*\n(.+)'
reg = re.compile(EXPR)


def parse(text):
    # get highlights
    highlights = []

    matches = reg.findall(text)
    for match in matches:
        title, authors, pages, _, _, date, text = match

        book = Book(title, authors.split(';'))
        highlight = Highlight(book, int(pages), datetime.strptime(date, "%d %B %Y %H:%M:%S"), text)

        highlights.append(highlight)
    
    return highlights
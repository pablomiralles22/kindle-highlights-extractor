import os
import sys
from datetime import datetime
from utils import parser

# app.py INPUT_FILE OUTPUT_DIRECTORY

assert(len(sys.argv) == 3)
in_file, out_dir = sys.argv[1:]

metadata_filepath = os.path.join(out_dir, '.date_run')

# get last date the script was run on
exists_last_run = os.path.isfile(metadata_filepath)
if exists_last_run:
    with open(metadata_filepath, 'r+') as metadata_file:
        date_str = metadata_file.read().strip()
        if date_str:
            last_run_date = datetime.fromisoformat(date_str)



# get text from file
f = open(in_file, 'r')
text = f.read()
f.close()

# get highlights
highlights = parser.parse(text)

# group highlights
groups = {}
for highlight in highlights:
    groups[highlight.book] = groups.get(highlight.book, [])
    groups[highlight.book].append(highlight)



for [book, highlights] in groups.items():
    title = book.format()

    out_filename = '{}.md'.format(title)
    out_filepath = os.path.join(out_dir, out_filename)
    out_file = open(out_filepath, 'a')

    for highlight in highlights:
        if not exists_last_run or highlight.date > last_run_date:
            print(highlight.format(), file=out_file)
            print('----------', file=out_file)

    out_file.close()


# store current run in date file
with open(metadata_filepath, 'w') as metadata_file:
    print(datetime.now().isoformat(), file=metadata_file)
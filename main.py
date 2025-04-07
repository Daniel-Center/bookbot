from stats import count_words
from stats import char_count
from stats import pretty_report
import sys

arg = sys.argv
if len(arg) !=2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    p = arg[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
    # do something with f (the file) here
    # f is a file object
        file_contents = f.read()
    return file_contents


def main(path_to_file):
    file = get_book_text(path_to_file)
    pretty_report(file)
main(p)
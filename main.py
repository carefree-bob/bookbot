import os
import sys

from stats import get_words, get_frequencies

header1 = "============ BOOKBOT ============"
header2 = "----------- Word Count ----------"
header3 = "--------- Character Count -------"
header4 = "============= END ==============="


usage = "Usage: python3 main.py <path_to_book>"

def get_book_text(bk_path):
    with open(bk_path, 'r') as fp:
        res = fp.read()
    return res


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print(usage)
        sys.exit(1)

    else:
        path_ = sys.argv[1]

    data = get_book_text(path_)
    word_c = len(get_words(data))

    if data is None:
        print(f"No data found")
    else:
        print(header1)
        print(f"Analyzing book found at {path_}...") 
        print(header2)
        print(f"Found {word_c} total words")
        print(header3)
        [print(f"{l}: {c}") for (l,c) in get_frequencies(data)]
        print(header4)



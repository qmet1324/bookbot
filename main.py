import sys
from stats import get_num_words
from stats import get_num_chars
from stats import get_char_list
from stats import print_report


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    file_contents = get_book_text(file_path)
    words_counter = get_num_words(file_contents)
    char_dict_counter = get_num_chars(file_contents)
    char_list = get_char_list(char_dict_counter)
    print_report(file_path, words_counter, char_list)


main()

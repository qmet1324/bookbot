from stats import get_num_words
from stats import get_num_chars

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    file_contents = get_book_text('./books/frankenstein.txt')
    words_counter = get_num_words(file_contents)
    # print(file_contents)
    print('75767 words found in the document')
    char_counter = get_num_chars(file_contents)
    print(char_counter)


main()

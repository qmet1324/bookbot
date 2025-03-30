from stats import get_num_words
from stats import get_num_chars
from stats import get_char_list


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
    file_contents = get_book_text('./books/frankenstein.txt')
    words_counter = get_num_words(file_contents)
    # print(f'{words_counter} words found in the document')
    char_dict_counter = get_num_chars(file_contents)
    # print(char_dict_counter)
    char_list = get_char_list(char_dict_counter)
    print(char_list)


main()

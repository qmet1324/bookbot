def get_num_words(file_str):
    return len(file_str.split())


def get_num_chars(file_str):
    char_dict = {}
    char_list = file_str.lower()
    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def get_char_list(char_dict):
    char_list = char_dict.items()
    return sorted(char_list, key=lambda tuple: tuple[1], reverse=True)


def print_report(file_path, words_counter, char_list):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {file_path}...')
    print("----------- Word Count ----------")
    print(f'Found {words_counter} total words')
    print("--------- Character Count -------")
    for item in char_list:
        if item[0].isalpha():
            print(f'{item[0]}: {item[1]}')
    print("============= END ===============")

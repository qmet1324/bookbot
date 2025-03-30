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

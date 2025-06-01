def get_word_count(contents):
    word_list = contents.split()
    word_count = 0
    for word in word_list:
        word_count += 1
    return word_count

def get_character_count(contents):
    contents = contents.lower()
    char_count = {}

    for char in contents:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_character_count(char_count):
    filtered_char_count = {char: count for char, count in char_count.items() if char.isalpha()}
    sorted_char_count = sorted(filtered_char_count.items(), key=lambda item: item[1], reverse=True)
    formatted_char_count = [f"{char}: {count}" for char, count in sorted_char_count]
    return formatted_char_count
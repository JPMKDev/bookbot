def get_book_text(filepath):
    fire_contents = None
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words(str):
    return len(str.split())

def count_chars(str):
    chars_dict = {}
    for char in str.lower():
        if char not in chars_dict:
            chars_dict[char] = 1
        else:
            chars_dict[char] += 1
    return chars_dict

def sort_on(char_count_dict):
    return char_count_dict["count"]

def sort_counts(chars_dict):
    char_dicts_list = []
    for char in chars_dict:
        char_dicts_list.append({"char":char, "count":chars_dict[char]})
    char_dicts_list.sort(reverse=True, key=sort_on)
    return char_dicts_list

def print_report(word_count, char_counts, target):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {target}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_count in char_counts:
        if char_count["char"].isalpha():
            print(f"{char_count["char"]}: {char_count["count"]}")
    print("============= END ===============")
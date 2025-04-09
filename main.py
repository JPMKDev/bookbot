from stats import *

target = "books/frankenstein.txt"

def main():
    text = get_book_text(target)
    #print(text)
    #print(f"{count_words(text)} words found in the document")
    #print(count_chars(text))
    char_counts = count_chars(text)
    sorted_char_counts = sort_counts(char_counts)
    print_report(count_words(text), sorted_char_counts, target)

main()
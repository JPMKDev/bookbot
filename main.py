from stats import *
import sys



def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    target = sys.argv[1]
    text = get_book_text(target)
    #print(text)
    #print(f"{count_words(text)} words found in the document")
    #print(count_chars(text))
    char_counts = count_chars(text)
    sorted_char_counts = sort_counts(char_counts)
    print_report(count_words(text), sorted_char_counts, target)

main()
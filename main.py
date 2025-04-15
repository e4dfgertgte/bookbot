import sys
from stats import get_num_words, get_num_char, sort_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        content_path = sys.argv[1]
        content_book = get_book_text(content_path)
#       print(content_book)
#       print(get_num_words(content_book), "words found in the document")
        print("Found", get_num_words(content_book), "total words")
#       print(get_num_char(content_book))
        sort_char(get_num_char(content_book))

"""
    def sort_on(vehicles):
        return vehicles.values()

    my_list = [1, 2, 3453, 6, 45, 3]
#    my_list.sort(reverse=True, key=sort_on)
    print(my_list)

    ve_list = []
    vehicles = {"e": 123, "f": 7}
    for a, b in vehicles.items():
        print(a, b)
#        ve_list.append(a, b)
    
    # ve_list = list(vehicles)


    print("ve_l", ve_list)
    
    dict_values = list(vehicles.values())
    dict_values.sort()
    print(dict_values)
"""

main()
def get_num_words(content_book):
    return len(content_book.split())

def get_num_char(content_book):
    char_dict = dict()
    counter = 1
    for char in content_book:
        if char.isalpha():
            char_l = char.lower()
            if char_l not in char_dict:
                char_dict.update({char_l: counter})
            else:
                char_dict[char_l] += 1
    return char_dict

#def sort_on(dict_sort):
#    return dict_sort.keys()
def sort_on(dict):
    return dict["num"]


def sort_char(char_dict):
    dict_list = []
    for char, num in char_dict.items():
        dict_list.append({"char": char, "num": num})
    dict_list.sort(reverse=True, key=sort_on)
    for d in dict_list:
        print(f"{list(d.values())[0]}: {list(d.values())[1]}")

"""
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
"""



#    sort_dict.sort(reverse=True, key=sort_on)
#    print(sort_dict)
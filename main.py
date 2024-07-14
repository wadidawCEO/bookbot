dic = {}

def main():
    text = "books/frankenstein.txt"
    file_content = get_book_text(text)
    count_words = get_total_words(file_content)
    each_characters = get_total_each_characters(file_content)
    print(f"--- Begin report of {text} ---")
    print(f"{count_words} words found in the document\n")
    for k,v in convert_dictionary_to_list(dic):
        print(f"The '{k}' character was found '{v}' times")

def get_book_text(text):
    # read the content in the specified file
    with open(text) as f:
        return f.read()

def get_total_words(file_content):
    # count the words in a text
    return len(file_content.split())

def get_total_each_characters(file_content):
    # change file_content to lowercase, then input it in dic with loop
    # it adds only the alphabet string in list_words to dic
    list_words = file_content.lower()
    for i in list_words:
        if i in dic:   
            dic[i] += 1
        elif i.isalpha() == True:
            dic[i] = 1
        else:
            pass
    return dic

def convert_dictionary_to_list(dic):
    # convert dic to list, then reverse sort it based on its value 
    temp_dic = dic.items()
    sorted_result = sorted(temp_dic, key=lambda d: d[1], reverse=True)
    return sorted_result
 
if __name__ == "__main__":
    main()
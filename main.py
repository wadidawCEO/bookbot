def main():
    text = "books/frankenstein.txt"
    file_content = get_book_text(text)
    count_words = get_total_words(file_content)
    each_characters = get_total_each_characters(file_content)

def get_book_text(text):
    # read the content in the specified file
    with open(text) as f:
        return f.read()

def get_total_words(file_content):
    # count the words in a text
    return len(file_content.split())

def get_total_each_characters(file_content):
    # change file_content to lowercase and split every strings into list;
    # double loop the result and adding it in dictionary
    dic = {}
    list_words = file_content.lower().split()
    for i in list_words:
        for k in i:
            if k in dic:   
                dic[k] += 1
            else:
                dic[k] = 1
    return dic
 
if __name__ == "__main__":
    main()
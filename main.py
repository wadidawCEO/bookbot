def main():
    text = "books/frankenstein.txt"
    file_content = get_book_text(text)
    count_words = get_total_words(file_content)
    print(count_words, "assasa")

def get_book_text(text):
    # read the content in the specified file
    with open(text) as f:
        return f.read()

def get_total_words(file_content):
    # count the words in a text
    return len(file_content.split())

if __name__ == "__main__":
    main()
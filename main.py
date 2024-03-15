def main():
    with open("/Users/joshuafierro/workspace/github.com/Jdfierro1/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
    # The above shows all text of the .txt file.
    # below begins the process to count the words of the file
    frankenstein = "/Users/joshuafierro/workspace/github.com/Jdfierro1/bookbot/books/frankenstein.txt"
    text = get_book_text(frankenstein)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document!")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

#### This was my first attempt below. Above is refined approach. ### 
   # with open("/Users/joshuafierro/workspace/github.com/Jdfierro1/bookbot/books/frankenstein.txt") as f:
   #     file_contents = f.read()
   # print(file_contents)
   # words = file_contents.split()
   # print(f"This book has {len(words)} words!")

main()
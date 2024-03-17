def read_text():
    # This function reads the text of a called file and returns it as a string 
    with open("/Users/joshuafierro/workspace/github.com/Jdfierro1/bookbot/books/frankenstein.txt") as f:
        text = f.read()
    return text 

def count_words(text):
    # Count the number of words in the book and return it at the end
    words = text.split()
    return f"{len(words)} words found in the document."

def count_letters(text):
    # This will count the unique count of letters in the book, all lower case 
    letters = {}
    text = text.lower()
    for words in text:
        if words.isalpha():
            letters[words] = letters.get(words, 0) + 1
    sorted_letters = list(letters.items())
    sorted_letters.sort(key=lambda x: x[1], reverse=True)
    return sorted_letters

def main():
    text = read_text()
    if text is not None:
        print("--- Begin report of books/frankenstein.txt ---")
        word_count = count_words(text)
        print(word_count)
        character_count = count_letters(text)
        for char, count in character_count:
            print(f"The '{char}' character was found {count} times")
        print("--- End report ---")
main()
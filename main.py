def main():
    with open("/Users/joshuafierro/workspace/github.com/Jdfierro1/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    words = file_contents.split()
    print(f"This book has {len(words)} words!")

main()
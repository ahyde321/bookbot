
def main():
    book_file = "books/frankenstein.txt"
    text = get_book_text(book_file)
    word_count = count_words(text)
    letter_count = count_letters(text)
    report = create_report(letter_count)

    print(f"--- Begin report of {book_file} ---")
    print(f"{word_count} words found in document")
    print(report)
    print("--- End report ---")
    # print(text)
    # print(f"{word_count} words found in file")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    count = len(words)
    return(count)

def count_letters(text):
    letters = {}
    for i in text.lower():
        if i in letters:
            letters[i] += 1
        else:
            letters[i] = 1
    return letters

def create_report(dict):
    list_of_tuples = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    report = ""
    for key, value in list_of_tuples:
        if key.isalpha():
            report += f"\nThe {key} character was found {value} times"
        
    return report

main()
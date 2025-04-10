def count_words(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    return word_count
    
def main():
    return print(f"{count_words('./books/frankenstein.txt')} words found in the document")
main()
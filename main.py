def main():
    book_path = "books/frankenstein.txt"
    contents = get_contents(book_path)
    char_dict = char_count(contents)
    #insert functions to run below
    #print(f"The word count is: {word_count(contents)}!")
    print(f"The character count is: {char_count(contents)}")


def get_contents(path):
    with open(path) as f:
        return f.read()

#with open("books/frankenstein.txt") as f:
    #file_contents = f.read()
    #print(file_contents)
    #...

#method for counting words
def word_count(text):
    num_of_words = 0
    #the textfile of "frankenstein" is one single string!
    #we'll use the .split() method to turn it into a list of x words. spliting at the white spaces.
    words = text.split() 
    #because words is also a list, we can use the len() function to grab the word count!
    for word in words:
        num_of_words += 1

    return num_of_words

def char_count(text):
    chars = {}
    lowercase_text = text.lower()

    for char in lowercase_text:
        #print(char)
        if char not in chars:
            chars[char] = 0

        chars[char] += 1

    return chars

# make a report() function that prints the title of the book, wordcount, and character counts!
def report()



main()
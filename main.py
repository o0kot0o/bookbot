class Book:
    def __init__(self, book_file):
        self.__book_file = book_file
        with open(self.__book_file) as f:
            self.__book_text = f.read()

    def count_words(self):
        return len(self.__book_text.split())
    
    def count_letters(self):
        letter_dic = {}
        for word in self.__book_text.split():
            word = word.lower()
            for letter in word:##
                if letter in letter_dic:
                    letter_dic[letter] += 1
                else:
                    letter_dic[letter] = 1
        return letter_dic
    
    def get_report(self):
        words_found = self.count_words()
        letters_found = self.count_letters()
        char_list = list(letters_found.items())
        char_list.sort()

        print(f"--- Begin report of {self.__book_file}")
        print(f"{words_found} words found in the document")
        print("")
        for item in char_list:
            char = item[0]
            count = item[1]
            if char.isalpha():
                print(f"The '{char}' character was found {count} times")
        print("--- End report ---")



book = "books/frankenstein.txt"

book1 = Book(book)

print(book1.get_report())

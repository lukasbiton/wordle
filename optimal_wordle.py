'''
A search for a general solution to the question posed by duotrigordle:
For a given length of word, with n words to guess and p guesses, is there
some form of optimal n and p?
Extra credit: for any word length?
Words found here: https://github.com/dwyl/english-words
'''

import numpy as np


def word_generator(path, len_word = 5):
    '''
    Make a generator to not have the whole json in memory
    at once.
    Words are stored one by one on a line with a \n at the
    end of each line.
    Use generator comprehension.
    '''

    with open(path, 'r') as file:
        return (row.rstrip() for row in open(path) if len(row.rstrip()) == len_word)


def letter_to_index(letter):
    '''
    Use ord to get the unicode character's ID.
    ord('a') returns 97, so just return ord - 97 to get the index
    for the numpy array.
    '''

    return ord(letter) - 97

def count_letters(len_word):
    '''
    Make a 5 by 26 numpy array and count how often each letter appears in order.
    Divide by the total number of words in the generator.
    '''

    words = word_generator('/home/lukas/Desktop/wordle/words.txt')
    letters_array = np.zeros([26,5])
    word_counter = 0

    while True:
        try:
            current_word = next(words)

            for letter, letter_spot in zip(current_word, range(len(current_word))):

                letters_array[letter_to_index(letter), letter_spot] += 1

            word_counter += 1

        except StopIteration: # When the generator is empty
            break

    return letters_array/(word_counter * ) # Because there are 5 letters in each word

if __name__ == '__main__':
    letters_array = count_letters()
    print(letters_array.sum().sum())

'''
A search for a general solution to the question posed by duotrigordle:
For a given length of word, with n words to guess and p guesses, is there
some form of optimal n and p?
Extra credit: for any word length?
Words found here: https://github.com/dwyl/english-words
'''

import numpy


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


def count_letters():
    '''
    Make a 5 by 26 numpy array and count how often each letter appears in order.
    Divide by the total number of words in the generator.
    '''

    words = word_generator('/home/lukas/Desktop/wordle/words.txt')

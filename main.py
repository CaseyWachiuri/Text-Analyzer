#!/usr/bin/python

'''
'''
import sys
import re
from pythonAssessment import *

def main():
    # declaring file path
    file = './News Article for Python Assessment.txt'

    # Opening the file for reading and loading text variable
    try:
        with open(file, 'r', encoding='utf-8') as openfile:
            text = openfile.read()
    # Error handling for the file
    except IOError as e:
        print( "I/O error({0}): {1}".format(e.errno, e.strerror) )
        return
    except:
        print("Unexpected error:", sys.exc_info()[0])
        return

    print('Text file opened successfully!!!')

    count_specific_word("", text)
    identify_most_common_word(text)
    calculate_average_word_length(text)
    count_paragraphs(text)
    count_sentence(text)

    # print(f"the value of name is: {repr(__name__)}")

if __name__ == "__main__":
    main()

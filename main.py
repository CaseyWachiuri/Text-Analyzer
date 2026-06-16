#!/usr/bin/python

'''
'''
from pythonAssessment import *
import re

def main():
    # Opening the file for reading and loading text variable
    with open('./News Article for Python Assessment.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    # Check if it opened successfully
    if not text:
        print(f'Failed to open text file')
        return

    print('Text file opened successfully!!!')

    # count_specific_word("ACME", text)
    print(identify_most_common_word(text))

    # print(f"the value of name is: {repr(__name__)}")

if __name__ == "__main__":
    main()

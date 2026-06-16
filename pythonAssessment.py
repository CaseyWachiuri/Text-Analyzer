#!/usr/bin/python3

import re
from collections import Counter

def count_specific_word(search, text_file):
    words = re.findall(r'\b\w+\b', text_file.lower())
    result = words.count(search.lower())
    if not result:
        return 0

    return result

def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    
    if not words:
        return None

    counts = Counter(words)
    return counts.most_common()
    # return the most common word as a string
    # An empty string should return None

# def calculate_average_word_length(str):
#     # take in str and return the average word length as float
#     # exclude punctuation marks and special characters from the word length (probably use has and all)
#     # return 0 for empty string
# 
# def count_paragraphs():
#     # take in a string and return the number of paragraphs as an integer
#     # define paragraphs based on empty lines between blocks of text
#     # display the count of paragraphs
#     # an empty string should return 1
# 
# def count_sentence(str):
#     # take in a string and return the number of sentences as an integer
#     # define sentences based on punctuation marks such as periods, exclamation marks, question marks
#     # display count of sentences
#     # an empty string should return 1

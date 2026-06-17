#!/usr/bin/python3

import re
from collections import Counter

def count_specific_word(text, search):
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
    result = words.count(search.lower())
    if not result:
        return 0

    return result

def identify_most_common_word(text):
    words = re.findall(r'\b\w+\b', text.lower())
    
    if not words:
        return None

    counts = Counter(words).most_common(1)[0][0]
    return counts

def calculate_average_word_length(text):
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())

    if not words:
        return 0

    total_length = sum(len(word) for word in words)
    return total_length/len(words)

def count_paragraphs(text):
    '''
    Return the number of paragraphs
    Paragraphs are separated by one or more empty lines
    Return 1 for any empty string
    '''

    if not text.strip():
        return 1
    else:
        paragraphs = re.split(r'\n\s*\n', text.strip())
        return len(paragraphs)


def count_sentences(text):
    '''
    Return the number of sentences
    Sentences end with ., ! or ?.
    Return 1 for an empty string
    '''
    if not text.strip():
        return 1

    sentences = [s for s in re.split(r'[.!?]+', text) if s.strip()]
    return len(sentences)

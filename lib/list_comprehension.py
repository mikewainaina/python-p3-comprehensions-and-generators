#!/usr/bin/env python3

def return_evens(num_list):
    return [y for y in num_list if y % 2 == 0]

def make_exclamation(sentence_list):
    return[sentence +"!" for sentence in sentence_list]
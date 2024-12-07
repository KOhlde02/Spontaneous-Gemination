"""
The goal of this file is to gather data to determine whether spontaneous
gemination happens more frequently following a u vowel than in general.
"""

import pandas as pd
from Draw_Better import get_preceding_vowel, extra_filter

# unicode representation of Hebrew vowels
hebrew_vowels = ["\u05B8", "\u05B7", "\u05B6", "\u05B5", "\u05B4", "\u05BB",
    "\u05BC", "\u05B9", "\u05B0", "\u05B1", "\u05B2", "\u05B3"]

def get_preceding_vowel_index(word, index):
    """
    This is a modification of the get preceding vowel function that finds the
    preceding vowel of a letter given its index. This allows for running the
    function multiple times on the same word in order to get the vowel preceding
    each instance of the letter.

    Inputs:
        word (str): the word for which we want to find the preceding vowel of an
        index
        index (int): the index of the letter for which to find the preceding
        vowel

    Output:
        vowel (str): the vowel preceding the indexed letter in the word.
    """
    # getting the part of the word before the letter of interest
    before_letter = word[:index]

    # iterating backwards through the part of the word before the given letter
    for char in reversed(before_letter):
        if char in hebrew_vowels:       # gets first vowel found
            vowel = char
            return vowel
    
    return None     # returns None if no vowels found


def get_u_vowels(df):
    """
    Given a dataframe with "Root" and "BHSA" columns, returns a dataframe with
    only entries for which there is a u vowel before the final root consonant.
    If a row in the dataframe does not have a root, the row is not dropped.

    Input:
        df (DataFrame): the original dataframe

    Output:
        df_u_vowels (DataFrame): a dataframe with only entries with u vowels
        preceding the last root consonant.
    """

    rows_to_drop = []
    u_vowels = {"\u05BC", "\u05BB"}     # storing rows to drop as a set

    for i, row in df.iterrows():
        if row["Root"].notna():     # does the following procedure for each row with root
            root = str(row["Root"])     # defining root and word
            word = str(row["BHSA"])
            last_root_cons = root[-1]   # getting last root consonant

            """
            Getting the indices where the last root consonant occurs in the
            word.
            """
            indices = [i for i, c in enumerate(word) if c == last_root_cons]
            preceding_vowels = set()    # storing preceding vowels as a set

            # Gets preceding vowel for each instance of the last root consonant
            if len(indices) > 0: 
                for j in sorted(indices): 
                    vowel = get_preceding_vowel_index(word, j)
                    preceding_vowels.add(vowel)

            """
            Takes set intersection of the preceding vowels and u vowels, drops
            the row if the intersection is empty.
            """
            if len(preceding_vowels & u_vowels) == 0:
                rows_to_drop.append(i)
        
        # dropping rows and returning the dataframe
        df_u_vowels = df.drop(rows_to_drop)
        
        return df_u_vowels
        
# filtering out rows with no given root
root_only = extra_filter[extra_filter["Root"].notna()]

# gets dataframe with only words with a u vowel preceding the last root consonant
df_u_vowels = get_u_vowels(root_only)

# taking a sample of 300
u_vowel_sample = df_u_vowels.sample(n=300, random_state=6)

# exporting to csv
u_vowel_sample.to_csv("u_vowel_sample.csv")
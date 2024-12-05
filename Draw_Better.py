"""
The goal of this file is to filter the data better than in Drawing_Samples.py
based on a few observations:
    - spontaneous gemination doesn't seem to be happening in hollow roots
    - with some exceptions, spontaneous gemination is preceded by a short vowel.
    - For nouns with no root listed, we can filter out entries with length less
        than three letters (since we need strong middle and third root constants
        with a suffix)
"""

import pandas as pd
from SponGem import find_spon_gem

# unicode representation of Hebrew vowels
hebrew_vowels = ["\u05B8", "\u05B7", "\u05B6", "\u05B5", "\u05B4", "\u05BB",
    "\u05BC", "\u05B9", "\u05B0", "\u05B1", "\u05B2", "\u05B3"]

def get_preceding_vowel(word, letter):
    """
    Given a Hebrew word and a letter, this function will return the preceding
    vowel. This function works with Hebrew text that includes cantillation
    marks.

    Inputs:
        word (str): A Hebrew word, including consonants, vowels, and possibly
        cantillation marks.
        letter (str): a single Hebrew consonant

    Output:
        vowel (str): the preceding vowel. Returns None if the letter or
        consonant not found.
    """

    # checks if the given letter is in the given word, records its index if so
    if letter in word:
        index = word.index(letter)
    else:
        return None

    # getting the part of the word before the letter of interest
    before_letter = word[:index]

    # iterating backwards through the part of the word before the given letter
    for char in reversed(before_letter):
        if char in hebrew_vowels:       # gets first vowel found
            vowel = char
            return vowel
    
    return None     # returns None if no vowels found

def get_following_vowel(word, letter):
    """
    Given a Hebrew word and a letter, this function will return the following
    vowel. This function works with Hebrew text that includes cantillation
    marks.

    Inputs:
        word (str): A Hebrew word, including consonants, vowels, and possibly
        cantillation marks.
        letter (str): a single Hebrew consonant

    Output:
        vowel (str): the following vowel. Returns None if the letter or
        consonant not found.
    """
     # checks if the given letter is in the given word, records its index if so
    if letter in word:
        index = word.index(letter)
    else:
        return None

    # getting the part of the word before the letter of interest
    after_letter = word[index+1:]

    # iterating through the word to find the next vowel
    for char in after_letter:
        if char in hebrew_vowels:       # gets first vowel found
            vowel = char
            return vowel
    
    return None     # returns None if no vowels found

def filter_for_spon_gem(df):
    """
    This function is designed to better filter a dataframe for instances where
    spontaneous gemination can happen.

    Input:
        df (DataFrame): the original dataframe to be filtered, must contain
        "Root" column

    Output:
        filtered_df (DataFrame): the dataframe better filtered for instances
        of spontaneous gemination.
    """

    rows_to_drop = []
    hollow = ["ו", "י"]
    schwa = "\u05B0"

    for i, row in df.iterrows():  # iterating though each row

        root = str(row["Root"])     # recording the word and the root
        word = str(row["BHSA"])

        if row["Root"] == "nan":       # for words with no root, drops if too short
            if len(word) < 5:
                rows_to_drop.append(i)
        elif len(root) > 2:
            sec_root_cons = root[-2]
            third_root_cons = root[-1]
            if sec_root_cons in hollow:         # drops hollow roots
                rows_to_drop.append(i)

            # checks following vowel if second root consonant occurs only once
            if word.count(sec_root_cons) == 1: 
                vowel = get_following_vowel(word, sec_root_cons)
                if vowel == schwa:
                    rows_to_drop.append(i)

            # checks preceding vowel if third root consonant occurs only once     
            elif word.count(third_root_cons) == 1:
                vowel = get_preceding_vowel(word, third_root_cons)
                if vowel == schwa:
                    rows_to_drop.append(i)

    filtered_df = df.drop(rows_to_drop)     # dropping rows

    return filtered_df      # returning the filtered dataframe

# importing csv file
bhs_nouns_final = pd.read_csv("bhs_nouns_final.csv")

# performing the filter
extra_filter = filter_for_spon_gem(bhs_nouns_final)

# taking the sample
bhs_better_sample = extra_filter.sample(n=750, random_state=4)

# exporting to csv
bhs_better_sample.to_csv("better_sample.csv")

# filtering out elements with possible spontaneous gemination
filtered_better_sample = find_spon_gem(bhs_better_sample)

# exporting to csv
filtered_better_sample.to_csv("filtered_better_sample.csv")


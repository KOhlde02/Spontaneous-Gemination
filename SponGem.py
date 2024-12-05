"""
This file processes a sample to help determine in which elements spontaneous
gemination occurs.
"""

import pandas as pd


def find_spon_gem(sample):
    """
    This function helps to find spontaneous gemination in a sample by filtering
    the sample in the following way:
        - For elements with a listed root, removes any elements that do not
        contain the last root consonant with a dagesh.
        - For elements without a listed root, removes any elements that do not
        contain a dagesh.
    This filtering is 100% sensitive but less specific to spontaneous
    gemination.

    Input:
        sample (DataFrame): the sample dataframe, must contain a "Root" column
        and a "Word" column

    Output:
        candidates (DataFrame): a dataframe which has elements that may contain
        spontaneous gemination
    """
    dagesh = "\u05BC"
    rows_to_drop = []

    for i, row in sample.iterrows():
        root = str(row["Root"])
        word = str(row["BHSA"])
        
        if root != "nan":        # case when the word has a listed root
            last_letter = root[-1]
            gemination = last_letter + dagesh
            if not gemination in word:      # drops the row if no gemination of last root letter
                rows_to_drop.append(i)
        else:
            if dagesh not in word:      # drops the row if word does not contain a dagesh
                rows_to_drop.append(i)
    
    candidates = sample.drop(rows_to_drop)
    return candidates

bhs_csv = pd.read_csv("bhs_sample.csv")     # reading in the sample csv

filtered_sample = find_spon_gem(bhs_csv)    # identifying spontaneous gemination

filtered_sample = filtered_sample[["Root", "BHSA", "extendedStrongNumber"]]   # relevant columns

filtered_sample.to_csv("filtered_sample.csv")


"""
The goal of this file is to gather data in order to determine if spontaneous
gemination happens more often in mem-preformative nouns than it does in nouns
generally.
"""

import pandas as pd
from Draw_Better import extra_filter

def get_mem_preform(df):
    """
    Given a dataframe, this function filters out rows with no given root, rows
    with a mem-initial root with less than two mems in the word, and rows
    with words which do not begin with mem.

    Input:
        df (DataFrame): the original dataframe with "Root" and "BHSA" columns.

    Output:
        df_mem_preform (DataFrame): the filtered dataframe
    """
    # filtering the dataframe to entries with a root
    df_root = df[df["Root"].notna()]

    # filtering the dataframe to entries where the word begins with mem
    df_mem = df_root[df_root["BHSA"].str.contains(">מ")]

    rows_to_drop = []

    for i, row in df_mem.iterrows():
        root = str(row["Root"])     # getting word and root
        word = str(row["BHSA"])
        # drops entries with root inititial mem and less than two mems in the word
        if root[0] == "מ":      
            if word.count("מ") < 2:
                rows_to_drop.append(i)
    
    # drops appropriate rows and returns dataframe
    df_mem_preform = df_mem.drop(rows_to_drop)
    
    return df_mem_preform

# filtering to entries with a root that are potential mem preformative nouns
mem_filter = get_mem_preform(extra_filter)

# taking a sample of 300
mem_sample = mem_filter.sample(n=300, random_state=5)

# exporting to csv
mem_sample.to_csv("mem_sample.csv")


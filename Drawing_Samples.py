import pandas as pd
import numpy as np
import zipfile

def add_root_column(bhs_nouns, strong_nouns):
    """
    Given the dataframe of BHS nouns and the dataframe of Strong's nouns,
    adds a root row for the dataframe of BHS nouns.

    Inputs:
        bhs_nouns (DataFrame): the dataframe of BHS nouns
        strong_nouns (DataFrame): the dataframe of Strong's nouns

    Output:
        bhs_nouns (DataFrame): the BHS nouns dataframe with a "Root" row from
            the Strong's nouns dataframe
    """

    bhs_nouns = bhs_nouns.copy()        # initialize a "Root" column
    bhs_nouns["Root"] = None

    for i, row in bhs_nouns.iterrows():
        strong_num = row["extendedStrongNumber"]
        strong_row = strong_nouns.loc[strong_nouns["#"] == strong_num]
    
        bhs_nouns.loc[i, "Root"] = strong_row.iloc[0]["Root"] # Get first root with matching Strong's

    return bhs_nouns


"""
Importing in csv file of all Hebrew words with Strong's numbers
"""
all_strongs = pd.read_csv("Strongs Numbers & glosses.csv")


"""
Extracting relevant columns and filtering down to only the nouns.
"""
strongs = all_strongs[["#", "Word", "Root", "Part of Speech" ]]
noun_types = ["noun masc", "noun fem", "n-e"]
strongs_all_nouns = strongs[strongs["Part of Speech"].isin(noun_types)]

"""
Filtering out geminate roots for all nouns which have roots listed.
"""
non_gem_nouns = strongs_all_nouns[strongs_all_nouns["Root"].str.get(-1) != strongs_all_nouns["Root"].str.get(-2)]


"""
Filtering out biconsonantal roots for all nouns which have roots listed.
"""
non_bicon_nouns = non_gem_nouns[non_gem_nouns["Root"].str.len() != 2]

"""
Filtering out roots with final guttural for all nouns with roots listed.
"""
gutturals = ["א", "ה", "ע", "ר", "ח"]
strong_nouns = non_bicon_nouns[~non_bicon_nouns["Root"].str.get(-1).isin(gutturals)]


"""
The above is the best filter we can do given the quality of the data. We first
filter by all nouns, then, for nouns with listed roots, we can filter out
biconsonantal roots, geminate roots and final guttural roots. Since very many
nouns do not have listed roots, this is a very rough filter, and the sample
will have to be filtered further.
"""

"""
Loading in the csv file of BHS with Strong's numbers.
"""
with zipfile.ZipFile('BHS-with-Strong-no-extended.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('temp_folder')

bhs = pd.read_csv('temp_folder/BHS-with-Strong-no-extended.csv', sep='\t')



"""
Filtering into words with only one root and converting the Strong's number into
a form that can be compared with the other csv (by removing the prefixing "H").
"""
bhs = bhs[bhs["extendedStrongNumber"].str.startswith("H")]  # this removes four anomalyous data points
bhs["extendedStrongNumber"] = bhs["extendedStrongNumber"].str[1:]
bhs = bhs[~bhs["extendedStrongNumber"].str.contains("H")]
bhs["extendedStrongNumber"] = bhs["extendedStrongNumber"].astype('int64')

"""
Filtering the BHS csv into only the nouns in the strong_nouns dataframe.
"""
bhs_nouns = bhs[bhs["extendedStrongNumber"].isin(strong_nouns["#"])]

"""
Adding a root column to the BHS spreadsheet
"""
bhs_nouns_final = add_root_column(bhs_nouns, strong_nouns)

"""
Drawing random samples from both BHS dataframe and the Strong's dataframe. For
the BHS sample, we are only interested in nouns for which spontaneous gemination
could occur. Thus, by sampling 500 rows, we hope to get a significant amount of
usable data points. For the Strong's dataframe, we will look at an entire noun
paradigm and expect to have more usable data points. So we only sample 100 rows.
"""
sample_bhs = bhs_nouns_final.sample(n=500, random_state=1)
sample_strongs = strong_nouns.sample(n=100, random_state = 2)

sample_bhs.to_csv("bhs_sample.csv")
sample_strongs.to_csv("strongs_sample.csv")
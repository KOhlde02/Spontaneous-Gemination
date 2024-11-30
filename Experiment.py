import pandas as pd
import numpy as np
import zipfile

all_strongs = pd.read_csv("Strongs Numbers & glosses.csv")
all_strongs10 = all_strongs[:10]
#print(all_strongs10[["#", "Gloss"]])

strongs = all_strongs[["#", "Word", "Root", "Part of Speech" ]]
noun_types = ["noun masc", "noun fem", "n-e"]
strongs_nouns = strongs[strongs["Part of Speech"].isin(noun_types)]
#print(strongs_nouns.size)

tricon_nouns = strongs_nouns[strongs_nouns["Root"].str.len() == 3]
#print(tricon_nouns)

gutturals = ["א", "ה", "ע", "ר", "ח"]
tricon_strong_nouns = tricon_nouns[~tricon_nouns["Root"].str.get(0).isin(gutturals)]
#print(tricon_strong_nouns)

"""
Tricon strong nouns is a dataframe that has all triconsonental nouns with a
non-guttural third root consonant and thus could be a candidate for spontaneous
gemination. We can use the Strong's concordance numbers of these nouns to
filter the dataframe of all of BHS and sample from that list. We can also sample
directly from the dataframe to get an idea of the proportion of nouns that show
spontaneous gemination somewhere in their paradigm.
"""

with zipfile.ZipFile('BHS-with-Strong-no-extended.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('temp_folder')

bhs = pd.read_csv('temp_folder/BHS-with-Strong-no-extended.csv', sep='\t')

bhs = bhs[bhs["extendedStrongNumber"].str.startswith("H")]
bhs["extendedStrongNumber"] = bhs["extendedStrongNumber"].str[1:]
bhs = bhs[~bhs["extendedStrongNumber"].str.contains("H")]
bhs["extendedStrongNumber"] = bhs["extendedStrongNumber"].astype('int64')

bhs_tricon = bhs[bhs["extendedStrongNumber"].isin(tricon_strong_nouns["#"])]
print(bhs_tricon.size)
print(bhs_tricon[:10])


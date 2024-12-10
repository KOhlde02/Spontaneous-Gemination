# Spontaneous-Gemination
Data analysis regarding the grammatical phenomenon of spontaneous gemination in Biblical Hebrew

Here are the files relevant to the paper and short description:

BHS-with-Strong-no-extended.csv: all words in BHS with Strong's numbers, from Open Hebrew Bible Project.
Draw_Better.py: Code for drawing the second sample with greater filtering
Drawing_Samples.py: Used to draw the original sample under the initial filtering
SponGem.py: This file contains the function which helps identify spontaneous gemination in a sample
Strongs Numbers & glosses.csv: This file contains all Strong's numbers with the part of speech and was used to filter the BHS .csv file to only contain nouns.
better_sample.csv: the sample obtained after the greater filtering in Draw_Better.py
bhs_nouns_final.csv: a dataset of nouns in BHS with filtering applied, to be passed and further filtered
bhs_sample.csv: the original sample obtained in Drawing_Samples.py
filtered_better_sample.csv: better_sample.csv filtered by the find_spon_gem function in SponGem.py
filtered_sample.csv: bhs_sample.csv filtered by the find_spon_gem function in SponGem.py
u_vowel_sample.csv: the sample of nouns with a u vowel preceding the final root consonant
uvowel.py: the file used to obtain a sample of nouns with a u-vowel before the final root consonant

Here is a brief description of the files not directly relevant to the paper:

Experiment.py: this was my original attempt at playing with the data to see if I thought I could actually do the estimation
GetSponGem.py: was originally going to be used to identify a large number of nouns with spontaneous gemination and observe certain properties
mem_sample.csv: a sample of mem-preformative nouns from nouns with listed roots, found that many of the nouns occurred many times in the dataset, making the analysis not very interesting
observeSG.csv: sample obtained in GetSponGem.py
premem.py: file used to obtain the sample of mem-preformative nouns in mem_sample.csv
strongs_sample.csv: sample obtained in Drawing_Samples.py by sampling from Strong's numbers instead of BHS, would need to do more work to analyze paradigms and estimate spontaneous gemination

Note the second set of files may not be well-documented

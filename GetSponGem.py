import pandas as pd
from SponGem import find_spon_gem
from Drawing_Samples import bhs_nouns_final

bhs_nouns_final.to_csv("bhs_nouns_final")
has_root = bhs_nouns_final[bhs_nouns_final["Root"].notna()]

big_sample = has_root.sample(n=2500, random_state=3)

get_spon_gem = find_spon_gem(big_sample)

get_spon_gem.to_csv("observeSG.csv")
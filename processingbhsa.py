import os
import pandas as pd 

locations = "~/github/ETCBC"
coreModule = "bhsa"
version = "2021"
tempDir = os.path.expanduser("{}/{}/_temp/{}/r".format(locations, coreModule, version))
os.mkdir("tempDir")
tableFile = "{}/{}{}.txt".format(tempDir, coreModule, version)
tableFilePd = "{}/{}{}.pd".format(tempDir, coreModule, version)
plainTextPd = "{}/plainTextFromPd.txt".format(tempDir)
plainTextR = "{}/plainTextFromR.txt".format(tempDir)

levelFeatures = """
    lex subphrase phrase_atom phrase clause_atom clause sentence_atom sentence
    half_verse verse chapter book
""".strip().split()
inLevelFeatures = ["in." + x for x in levelFeatures]

dtype = dict(
    n="int",
    otype="str",
    code="str",
    det="str",
    dist="float64",
    dist_unit="str",
    domain="str",
    function="str",
    g_cons="str",
    g_cons_utf8="str",
    g_lex="str",
    g_lex_utf8="str",
    g_nme="str",
    g_nme_utf8="str",
    g_pfm="str",
    g_pfm_utf8="str",
    g_prs="str",
    g_prs_utf8="str",
    g_uvf="str",
    g_uvf_utf8="str",
    g_vbe="str",
    g_vbe_utf8="str",
    g_vbs="str",
    g_vbs_utf8="str",
    g_word="str",
    g_word_utf8="str",
    gn="str",
    is_root="str",
    kind="str",
    language="str",
    languageISO="str",
    lex="str",
    lex_utf8="str",
    ls="str",
    mother_object_type="str",
    nme="str",
    nu="str",
    number="float64",
    pdp="str",
    pfm="str",
    prs="str",
    ps="str",
    rela="str",
    sp="str",
    st="str",
    tab="float64",
    trailer_utf8="str",
    txt="str",
    typ="str",
    uvf="str",
    vbe="str",
    vbs="str",
    vs="str",
    vt="str",
    g_qere_utf8="str",
    qtrailer_utf8="str",
    entry="str",
    entry_heb="str",
    entryid="str",
    freq_lex="float64",
    freq_occ="float64",
    g_entry="str",
    g_entry_heb="str",
    gloss="str",
    id="str",
    lan="str",
    nametype="str",
    pos="str",
    rank_lex="float64",
    rank_occ="float64",
    root="str",
    subpos="str",
    phono="str",
    phono_sep="str",
    book="str",
    chapter="float64",
    label="str",
    verse="float64",
    instruction="str",
    number_in_ch="float64",
    pargr="str",
    distributional_parent="str",
    functional_parent="str",
    mother="str",
)
for otype in inLevelFeatures:
    dtype[otype] = "float64"

naValues = dict((x, set() if dtype[x] == "str" else {""}) for x in dtype)

bhsa = pd.read_table(
    tableFile,
    delimiter="\t",
    low_memory=False,
    encoding="utf8",
    keep_default_na=False,
    na_values=naValues,
    dtype=dtype,
    #    index_col='n',
)



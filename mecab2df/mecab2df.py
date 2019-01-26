def parse(file):
    import numpy as np
    import pandas as pd
    import MeCab
    import text_preprocessing

    text_preprocessed = text_preprocessing.parse_text(file)
    m = MeCab.Tagger()
    morph_text = m.parse(text_preprocessed)
    morph_text = morph_text.split('\n')
    morph_text = morph_text[:-2]

    surfaces = []
    features_all = []
    for morph in morph_text:
        (surface, feature) = morph.split('\t')
        surfaces.append(surface)
        features_all.append(feature)

    features = []
    for features_line in features_all:
        feature = features_line.split(',')
        features.append(feature)

    surfaces_df = pd.DataFrame(surfaces)
    features_df = pd.DataFrame(features)
    morphs_df = pd.concat([surfaces_df, features_df], axis=1)
    morphs_df.reset_index(drop=True, inplace=True)
    morphs_df.columns = ['表層形', '品詞', '品詞細分類1', '品詞細分類2', '品詞細分類3', '活用型', '活用形', '原形', '読み', '発音']

    return(morphs_df)

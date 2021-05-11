import streamlit as st

import gensim.models as word2vec
import pandas as pd

model = word2vec.Word2Vec.load("dosukebe.model")

"""
# 類語探索
"""

user_input = ""
user_input = st.text_input("類義語のリストが欲しい単語を入力してください")
if user_input != "":
    similar = model.wv.most_similar(user_input)
    columns = ["類似する単語", "類似度"]
    DF = pd.DataFrame(similar)
    DF.columns = columns
    DF.set_index(columns[0])
    st.dataframe(DF)

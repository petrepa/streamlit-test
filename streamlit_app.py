import streamlit as st
import pandas as pd
import numpy as np

st.title("PETREPA's first streamlit test")


st.header("Dataframe")
st.caption("Here you can see a simple dataframe test using pandas and numpy")

df = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

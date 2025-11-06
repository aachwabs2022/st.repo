import streamlit as st
import numpy as np
import altair as alt
import pandas as pd

# st.header('st.write')

# df = pd.DataFrame({
#     'first column': [1, 2, 3, 4],
#     'second column': [10, 20, 30, 40]
#      })
# st.write('text above', df, 'text below')

# df = pd.DataFrame(
#     np.random.randn(200, 3),
#     columns=['a', 'b', 'c'])
# c = alt.Chart(df).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
# )
# st.write(c)

from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

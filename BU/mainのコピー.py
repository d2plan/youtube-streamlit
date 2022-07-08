import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



st.title('Streamlit 超入門')


st.write('Display Image')

img = Image.open('sample.jpg')
st.image(img, caption='myhome', use_column_width=True)

Image.open('sample.jpg')


#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50,50]+[35.47,136.20],
#    columns=['lat','lon']
#)

#st.table(df.style.highlight_max(axis=0))

#st.map(df)

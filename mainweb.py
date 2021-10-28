import streamlit as st
import pandas as pd
import numpy as np
st.write('hahahaha')





uploaded_file = st.file_uploader("上传一张图片", type="txt")

if uploaded_file is not None:
    data=uploaded_file.read()
    st.write(data)

import streamlit as st
from io import StringIO
from summarizer1 import summarizer
from summarizer2 import generate_summary
from pathlib import Path
import os

st.markdown("<h1 style='text-align: center;'>Text Summarizer</h1>",
            unsafe_allow_html=True)

text = st.text_area("Input Text For Summary (More than 200 words)", height=200)
col1,  col2, col3 = st.columns(3)
if col1.button('SUMMARIZE'):
    #try:
       
    
        textfile = open("content.txt","w")
        textfile.write(text)
        textfile.close()
        summary1=summarizer(text)
        summary2=generate_summary("content.txt")
        st.markdown("<h2> Your Summary : </h2>" ,  unsafe_allow_html=True)        
        st.markdown("<h3> > Summary 1 : </h3>" ,  unsafe_allow_html=True)                                
        st.write(summary1)
        st.markdown("<h3> > Summary 2 : </h3>" ,  unsafe_allow_html=True)
        st.write(summary2)
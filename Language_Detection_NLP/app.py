import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model


LrdetectFi1e= open('model.pckl','rb' )
Lrdetect_Model= pickle.load(LrdetectFi1e)
LrdetectFi1e.close()
st.title("Language Detection Tool")
input_test= st.text_input( "provide your text input here",'Hello my name is jay')

button_clicked= st.button( "Get Language Name")
if button_clicked:
    st.text(Lrdetect_Model. predict([input_test]))

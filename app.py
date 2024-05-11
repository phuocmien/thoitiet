import streamlit as st
st.set_page_config(layout='wide')
text = st.text_input("Nhập nội dung: ")
btn = st.button("Click")
if btn:
    st.write(f"Nội dung đã nhập: {text}")
    
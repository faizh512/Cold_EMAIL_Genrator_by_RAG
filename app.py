import streamlit as st
from main import Main_generator

st.title("📧 Cold Mail Generator")
url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-38066?from=job%20search%20funnel")
submit_button = st.button("Submit")

if submit_button:
    output = Main_generator.main_gen(url_input)  # No need to instantiate
    st.write(output)

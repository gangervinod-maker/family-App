import streamlit as st

st.set_page_config(page_title="Family Form", layout="centered")

st.title("👨‍👩‍👧‍👦 Family Information Form")

name = st.text_input("Your Full Name")
family_count = st.number_input("How many family members?", min_value=1, max_value=20, step=1)
address = st.text_area("Full Address")

if st.button("Submit"):
    st.success(f"Thanks {name}, your form is submitted!")

import urllib.request
import streamlit as st

@st.cache_data  # use st.cache if you're on an older version of Streamlit
def download1(url1):
    filename = url1.split('/')[-1]
    urllib.request.urlretrieve(url1, filename)
    return filename

# Example usage
url = "https://github.com/Anubhav1107/streamlit/releases/download/fasterrcnn.pth/fasterrcnn.pth"
download1(url)

st.write("File downloaded and cached.")

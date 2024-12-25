
import streamlit as st

pg = st.navigation([
    st.Page("pages/home.py", title="HOME"),
    st.Page("pages/classification.py", title="Klasifikasi Citra"),
    st.Page("pages/dashboard.py", title="CNN/VGG"),
    ])
pg.run()

import streamlit as st
from settings import *
from PIL import Image
col1,col2 = st.columns(2,gap='large')
with col1:
    st.markdown("# 📃 CV")
with col2:
    # Load CSS, PDF & Profile Pic

    with open(resume_file, 'rb') as pdf_file:
        PDFbyte = pdf_file.read()
    st.download_button(
        label = '📜 Download CV',
        data = PDFbyte,
        file_name = resume_file.name,
        mime = 'application/octet-stream'
    )

# Education
st.subheader('🏫 Education')
st.markdown(education,unsafe_allow_html=True)

st.divider()
# Experience & Qualifications
st.subheader('🧽 Relevant Work Expereince')
st.write(relevant_work_experience)

st.divider()
# Skills
st.subheader('⚒️ Skills & Tools')
# st.write("""
#          - 🧑🏽‍💻  Programming: Python (Pandas, Scikit Learn), SQL, C
#          - 📈  Data Visualization: Tableau, Excel, Google Sheets, Streamlit, Plotly, Matplotlib
#          - 🔮  Modeling: Linear & Logisitc Regression
#          """)

col1,col2,col3 = st.columns(3,gap='small')
with col1:
    st.button('Python')
    st.button('C/C++')
    st.button('SQL')
with col2:
    st.button('Streamlit')
    st.button('Tableau')
    st.button('Excel')

with col3:
    st.button('Linear Regression')
    st.button('Logistic Regression')

# Publications
st.divider()

# Publications and Posters
st.subheader('📰 Publications & Posters')
st.markdown(publications,unsafe_allow_html=True)

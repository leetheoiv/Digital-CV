import streamlit as st
from PIL import Image
from settings import *
st.markdown("# 👨🏽‍🎨 Projects")

st.markdown("### Data Visualization")
alert_db_pic = Image.open(alert_db_pic)
alert_title = '###### Employee Schedule Dashboard'
alert_caption = """
    A streamlit built dashboard that provides employee schedule statistics and
    scheduiling visualizations
    Tools: Python, Streamlit, SQL
    """
bffrs_title = '###### BFFRS Mental Health Dashboard'
bffrs_db_pic = Image.open(bffrs_db_pic)
bffrs_db_caption = """
    An Excel built
    Tools: Python,Excel
    """

db_links = ['[Schedule-Dahsboard](https://github.com/leetheoiv/Schedule-Dahsboard)','[BFFRS-MH-Dashboard](https://github.com/leetheoiv/BFFRS-Mental-Health)']
db_images = [alert_db_pic,bffrs_db_pic]
db_captions = [alert_caption,bffrs_db_caption]
db_titles = [alert_title,bffrs_title]
db_cols = st.columns(3,gap='large')
for i,image in enumerate(db_images):
    db_cols[i].markdown(db_titles[i],unsafe_allow_html=True)
    db_cols[i].image(image,caption=None)
    db_cols[i].write(db_links[i])

st.divider()
st.markdown("### Data Analytics")
analytics_links = ['[VR-Experiences](https://github.com/leetheoiv/vr-experiences/blob/main/EDA.ipynb)']
analytics_images = [vr_experiences]
analytics_captions = []
analytics_titles = ['###### VR Experiences Analytics']

# analytics_cols = st.columns(3,gap='large')
col1,col2,col3 = st.columns(3)
# for i,image in enumerate(analytics_images):
    # analytics_cols[i].markdown(analytics_titles[i],unsafe_allow_html=True)
    # analytics_cols[i].image(image,caption=None)
    # analytics_cols[i].write(analytics_links[i])
vr_experiences_pic = Image.open(vr_experiences)
with col1:
    st.markdown(analytics_titles[0], unsafe_allow_html=True)
    st.image(vr_experiences_pic)
    st.write(analytics_links[0])

st.divider()
st.markdown("### Data Modeling")
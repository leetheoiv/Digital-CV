import streamlit as st
from PIL import Image
from settings import *
# video to watch for tutorials: https://www.youtube.com/watch?v=BXAeMICmUSQ



st.set_page_config(page_title=page_title,page_icon=page_icon)


#Load CSS, PDF & Profile Pic

# Header Section
col1,col2 = st.columns(2,gap='small')
with col1:
    profile_pic = Image.open(profile_pic)
    st.image(profile_pic,width=300)

with col2:
    st.title("🙂 About Me")
    st.write(description)
    st.write(email)

st.write('#')
st.subheader("Social Links")
col1,col2,col3 = st.columns(3,gap='small')
# cols = st.columns(len(social_media))
# for index, (platform,link) in enumerate(social_media.items()):
#     cols[index].markdown(f'[{platform}]({link})')

with col1:
    st.markdown(social_media['linkdin'])
with col2:
    st.markdown(social_media['Github'])
with col3:
    st.markdown(social_media['Medium'])



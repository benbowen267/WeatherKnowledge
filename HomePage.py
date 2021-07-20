# HomePage.py
import streamlit as st
from datetime import datetime, timedelta
from pytz import timezone
import pytz
from pytz import common_timezones
Sydney = 'Australia/Sydney' in common_timezones
st.write(Sydney)
def app():
    col1, col2 = st.beta_columns([2.5,10])
#Header logo and Name
    with col1:
        st.image('unnamed.png')

    with col2:
        st.title("SHARED PATH ABORIGINAL AND TORRES STRAIT ISLANDER CORPORATION")
#App Name
    st.title('Welcome to the Indigenous Weather Knowledges App')
#Intro information HomePage
    st.write('Here at the Indigenous Weather Knowledges App we celebrate the traditional knowledges and lore that is the product of tens of thousands of years of scientific observations and custodianship.')
    st.write('Indigenous nations have used their scientific observations that are embedded into their lore to create sustainable ecosystems with realtionships based on balance.')
    st.write('Different Nations and language groups have different understandings and systems to define seasons on Country and the lore of plants, animals and realtionships that a governed and guided by the seasons.')
    st.write('Some Nations have two seasons and some have six and arguably more depending on their knowledge levels. Through actioning Indigenous knowledge systems we aim to put our Elders in the pilot seat to design, plan and implement strategies to best build custodianship over land to restore sustainability, balance, lore over land, water and sky country.')
#AITSIS map of Aus
    st.image('AIATSIS.jpg', caption = 'AIATSIS Map of Indigenous Australia')

#navigation buttom to enter App



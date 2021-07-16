import HomePage
import Warren
import streamlit as st
PAGES = {
    "Home Page": HomePage,
    "Warren" : Warren
}
st.sidebar.title('Navigation Pages')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
#app.run()
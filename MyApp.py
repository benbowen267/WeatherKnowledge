import HomePage
import Warren
import Naarm
import Ngunnawal
import Nipaluna
import Gimuy
import Mparntwe
import Tarndanya
import Boorloo
import streamlit as st
PAGES = {
    "Home Page": HomePage,
    "Warren" : Warren,
    "Naarm": Naarm,
    "Ngunnawal": Ngunnawal,
    "Nipaluna": Nipaluna,
    "Gimuy": Gimuy,
    "Mparntwe": Mparntwe,
    "Tarndanya": Tarndanya,
    "Boorloo": Boorloo,
    #"Rubibi": Rubibi,
    #"Garramilla": Garramilla,
    #"Meanjin": Meanjin
}
st.sidebar.title('Navigation Pages')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
#app.run()
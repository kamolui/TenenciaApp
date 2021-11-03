import streamlit as st
import numpy as np
from PIL import  Image

# Custom imports
from multipage import MultiPage
from pages import data_visualize, prediction, data_upload, metadata, first_page, full_pre

# Definir logo y titulo de la pagina
logo = Image.open('data/images/logo.png')
st.set_page_config(page_title='Predicción Tenencia', page_icon='logo')

# Ocultar menu y footer
hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

# Create an instance of the app
app = MultiPage()

# Title of the main page
display = Image.open('data/images/logo_dpfi-cdmx.png')
display = np.array(display)
st.image(display, width = 650)
st.title("Aplicación de predicción del pago de tenencia")
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
#col1, col2 = st.columns(2)
#col1.title("Creado por el area de *Inteligencia Fiscal*")
#col2.title("*Inteligencia Fiscal*")
st.title("Creado por el area de **Inteligencia Fiscal**")

# Add all your applications (pages) here
app.add_page("Pagina Principal", first_page.app)
app.add_page("Cargar datos", data_upload.app)
app.add_page("Cambiar datos", metadata.app)
app.add_page("Inferencia", prediction.app)
app.add_page("Predicciones", full_pre.app)
app.add_page("Data Analysis",data_visualize.app)

app.run()
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import joblib
import plotly.express as px
import os


# @st.cache
def app():
    st.write("""
    # Predicciones
    
    Haciendo uso de la base previamnete cargada, se realizaran las predicciones con dichos datos.
    """)

    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Por favor sube un archivo en la pagina `Cargar Datos`!")
    else:
        # cargar datos guardados en cache
        data = pd.read_csv('data/main_data.csv')
        st.dataframe(data)
        data.rename(columns={'deuda': 'deudas_antes_21'},
                  inplace=True)

        # Reads in saved classification model
        #model_gbc = GradientBoostingClassifier()      # parameters not required.
        #model_gbc.load_model('models/gradient_tenencia_definitivo_1.sav')
        model_1 = joblib.load('models/gradient_tenencia_definitivo_1.sav')

        #model_2 = xgb.Booster()
        #model_2 = joblib.load('models/xgb_tenencia.sav')

        #model_xgb_2 = xgb.Booster()
        #model_xgb_2.load_model("models/xgb_tenencia.sav")

        # Apply model to make predictions
        prediction = model_1.predict(data.drop(['nplaca', 'periodos'], axis=1))
        #prediction_proba = model_1.predict_proba(data)

        # Añadir la columna de predicciones
        data['prediccion'] = prediction

        # Añadir columna categorica con los resultados
        def tipo(cols):
            pago = cols[0]

            if pago == 1:
                tipo = 'Si pago'
            else:
                tipo = 'No pago'

            return tipo

        data['estatus_pago'] = data[['prediccion']].apply(tipo, axis=1)

        #st.subheader('Prediction')
        #contribuyente_tipo = np.array(['No pago','Si pago'])
        #st.write(contribuyente_tipo[prediction])

        #st.subheader('Prediction Probability')
        #st.write(prediction_proba)

        col1, col2 = st.columns(2)
        col1.subheader('Predicciones')
        col1.write(data[['nplaca', 'estatus_pago']])
        col2.subheader('Resultados')
        col2.write(data['estatus_pago'].value_counts())

        # graficar resultados
        fig = px.histogram(
            data_frame=data,
            x="prediccion",
            color='estatus_pago',
            title="Predicciones")

        fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',
        })

        st.plotly_chart(fig)

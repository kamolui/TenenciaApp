import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import joblib

def app():
    st.write("""
    # Predicciones
    """)

    st.header('Caracteristicas de entrada')


    # Collects user input features into dataframe
    def user_input_features():

        col1, col2, col3 = st.columns(3)
        ingresoAVG = col1.number_input('IngresoAVG', 0, 300000, 1000, step=1000)
        inicio = col2.slider('inicio', 2000, 2024, 2019, step=1)
        valor_factura = col3.number_input('Factura', 5000, 5000000, 100000, step=10000)

        col4, col5, col6 = st.columns(3)
        valor_depreciado = col4.number_input('Depreciacion', 500, 3000000, 5000, step=1000)
        potencial = col5.number_input('Faltante', 0, 250000, 1000, step=1000)
        deuda = col6.slider('Periodos no pagados', 0, 24, 1)

        col7, col8 = st.columns(2)
        subsudio = col7.number_input('Subsidio otorgado', 0, 8000, 1000, step=500)
        tenencia = col8.number_input('Tenencia al año actual', 0, 70000, step=1000)

        col9, col10, col11 = st.columns(3)
        tipo_persona = col9.selectbox('Tipo de persona', ('Persona Fisica', 'Persona Moral'))
        tarjeta_circulacion = col10.selectbox('Tarjeta de circulacion', ('Vencida', 'Vigente', 'sin tramitar'))
        uso = col11.selectbox('Tipo de uso', ('AUTO PARTICULAR', 'MOTOCICLETAS'))

        data = {'IngresoAVG': ingresoAVG,
                 'Inicio': inicio,
                 'Valor_factura': valor_factura,
                 'Tipo_persona': tipo_persona,
                 'Tarjeta_circulacion': tarjeta_circulacion,
                 'Descripcion_uso': uso,
                 'Valor_depreciado': valor_depreciado,
                 'Deuda' : deuda,
                 'Potencial' : potencial,
                 'Subsidio' : subsudio,
                 'Tenencia' : tenencia}
        features = pd.DataFrame(data, index=[0])
        return features

    input_df = user_input_features()

    # Displays the user input features
    st.subheader('Caracteristicas dadas por el usuario')

    df = input_df
    df.rename(columns={'Potencial': 'potencial_16_21', 'Tipo_persona': 'tipo_persona',
                       'Tarjeta_circulacion' : 'tarjeta_circulacion',
                       'Descripcion_uso' : 'desciprcion_uso', 'Valor_depreciado' : 'valor_depreciado_2021',
                       'Tenencia' : 'tenencia_2021', 'Subsidio' : 'subsidio_2021',
                       'Deuda' : 'deudas_antes_21', 'Valor_factura' : 'valor_factura'
                       }, inplace=True)


    st.write(df)

    l = ['Periodos_2021', 'IngresoAVG', 'Inicio', 'potencial_16_21',
         'valor_factura', 'tipo_persona', 'tarjeta_circulacion',
         'desciprcion_uso', 'valor_depreciado_2021', 'tenencia_2021',
         'subsudio_2021', 'deudas_antes_21']

    # Reads in saved classification model
    #model_gbc = GradientBoostingClassifier()      # parameters not required.
    #model_gbc.load_model('models/gradient_tenencia_definitivo_1.sav')
    model_1 = joblib.load('models/gradient_tenencia_definitivo_1.sav')

    #model_2 = xgb.Booster()
    #model_2 = joblib.load('models/xgb_tenencia.sav')

    #model_xgb_2 = xgb.Booster()
    #model_xgb_2.load_model("models/xgb_tenencia.sav")

    # Apply model to make predictions
    prediction = model_1.predict(df)
    prediction_proba = model_1.predict_proba(df)

    st.subheader('Prediction')
    contribuyente_tipo = np.array(['No pago','Si pago'])
    st.write(contribuyente_tipo[prediction])

    st.subheader('Prediction Probability')
    st.write(prediction_proba)


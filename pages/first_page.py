import streamlit as st


def app():
    st.markdown('''
       ---
    ''')

    st.title("Objetivo de la aplicacion")

    st.markdown("""
    Esta aplicación se utiliza como herramienta de estimación del pago de tenencia en la Ciudad de México.
    Utiliza métodos de __Machine Learning__ para inferir si el contribuyente realizara su pago o no, el modelo
    resultante fue entrenado con datos históricos recopilados por la secretaria.
    
    La aplicación toma un conjunto de datos que el usuario deberá cargar para realizar la predicción. La transformación
    y el pre procesado de datos estas automatizados para un uso más sencillo. Además de tener una sección donde se pueden
    realizar estimaciones individuales seleccionando los valores manualmente.
    
    Por último se muestran los resultados del entrenamiento del modelo y sus evaluaciones para medir el rendimiento del 
    modelo.

    """)

    st.markdown('''
    ---
    **Creditos:** App creada en Python + Streamlit por la [Secretaria de Administración y Finanzas de la CDMX](https://www.finanzas.cdmx.gob.mx) (aka [SAF](https://www.finanzas.cdmx.gob.mx))
    ''')

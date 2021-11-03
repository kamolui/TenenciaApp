import streamlit as st
from PIL import Image
import numpy as np


def app():
    st.title('Resultados del entrenamiento')
    st.markdown("""
    Se muestran las metricas de evaluacion del modelo, para entender mejor el rendimiento del 
    mismo. Ademas que se agregan graficas para facilitar la explicacion.
    """)

    col1, col2 = st.columns(2)

    col1.markdown("""
    Matriz de confusion modelo Gradient Boosting con datos de training
    """)
    col2.markdown("""
    Matriz de confusion modelo XGradient Boosting con datos de testing
    """)

    col3, col4 = st.columns(2)

    matrix_gbc = Image.open('data/images/gbc_matrix_train.png')
    matrix_gbc = np.array(matrix_gbc)
    col3.image(matrix_gbc, width=400)

    matrix_xgb = Image.open('data/images/gbc_matrix_test.png')
    matrix_xgb = np.array(matrix_xgb)
    col4.image(matrix_xgb, width=400)

    st.markdown("""
    ## Explicacion
    las matrices de confucion son una medida de desempeño para problemas de clasificacion
    donde las salidas pueden ser dos o mas clases. Es una tabla con 4 diferente combinaciones
    de valores reales y predecidos.
    """)

    con_matrix = Image.open('data/images/con_matrix.png')
    st.image(con_matrix, width=500)

    st.markdown(r"""
    Es extremadamente util ya que nos ayuda a calcular otras metircas como el Recall,
    Precision, Accuracy, etc.
    
    Expliquemos que es TP, TN, FP y FN; para nuestro problema del pago de tenencia (si y no).
    
    ### True Positive
    Predecir que es positivo y es verdadero.
    Predices que un contribuyente va a pagar y en realidad pagar.
    Predices que una mujer esta embarazda y ella en realidad esta embarazda.

    ### True Negative
    Predecir que es negativo y si es verdero.
    PRedices que un contribuyente no paga y en realidad no paga.
    Predices que un hombre no esta embarazado y en realidad no lo esta.
    
    ### False Positive (error tipo I)
    Predices que es positivo y es falso.
    Predices que un contribuyente va a pagar y en realidad no lo hace.
    Predices que un hombre esta embarazado y en realidad el no lo esta.
    
    ### False Negative (error tipo II)
    Predices que es negativo y es falso.
    Predices que un contribuyente no va a pagar u en verdad si paga.
    Predices que una mujer no esta embarazada pero en realidad si lo esta.
    
    Para el pago de la tenencia encontramos que es mas riesgoso para nosotros tener un gran numero de FP, es decir
    predecir que pagaran su tenencia cuando en realidad no lo hacen. Nos llevaria a estimaciones incorrectas y mas riesgosas.
    Es por eso que el modelo se construyo minimisando los FP dando mas improtancia a la metrica Precision ¿Pero que es el 
    Precision?
    
    ### Precision
    Precision = $\frac{TP}{TP+FN}$
    
    La ecuacion de arriba puede explicarse diciendo, de todos los datos que predicimos como positivos
    cuantos son en realidad positivos. Asi el Precision nos da en terminos de porcentaje la cantidad de
    predicciones de la clase positiva que son correctas, incrementar dicha metrica reduce el numero de FP.
    """)
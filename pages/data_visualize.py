import streamlit as st
from PIL import Image
import numpy as np


def app():
    st.title('Resultados del entrenamiento')
    st.markdown("""
        Se muestran las métricas de evaluación del modelo, para entender mejor el rendimiento del 
        mismo. Además que se agregan graficas para facilitar la explicación.
        """)

    col1, col2 = st.columns(2)

    col1.markdown("""
        **Matriz de confusión modelo Gradient Boosting con datos de training**
        """)
    col2.markdown("""
        **Matriz de confusión modelo XGradient Boosting con datos de testing**
        """)

    col3, col4 = st.columns(2)

    matrix_gbc = Image.open('data/images/gbc_matrix_train.png')
    matrix_gbc = np.array(matrix_gbc)
    col3.image(matrix_gbc, width=400)

    matrix_xgb = Image.open('data/images/gbc_matrix_test.png')
    matrix_xgb = np.array(matrix_xgb)
    col4.image(matrix_xgb, width=400)

    st.markdown("""
        ## Explicación
        las matrices de confusión son una medida de desempeño para problemas de clasificación
        donde las salidas pueden ser dos o más clases. Es una tabla con 4 diferentes combinaciones
        de valores reales y predichos.
        """)

    con_matrix = Image.open('data/images/con_matrix.png')
    st.image(con_matrix, width=500)

    st.markdown(r"""
        Es extremadamente útil ya que nos ayuda a calcular otras métricas como el Recall,
        Precision, Accuracy, etc.

        Expliquemos que es TP, TN, FP y FN; para nuestro problema del pago de tenencia (si y no).

        ### True Positive
        Predecir que es positivo y es verdadero.
        Predices que un contribuyente va a pagar y en realidad pagar.

        ### True Negative
        Predecir que es negativo y si es verdadero.
        Predices que un contribuyente no paga y en realidad no paga.

        ### False Positive (error tipo I)
        Predices que es positivo y es falso.
        Predices que un contribuyente va a pagar y en realidad no lo hace.

        ### False Negative (error tipo II)
        Predices que es negativo y es falso.
        Predices que un contribuyente no va a pagar u en verdad si paga.

        Para el pago de la tenencia encontramos que es más riesgoso para nosotros tener un gran número de FP, es decir
        predecir que pagaran su tenencia cuando en realidad no lo hacen. Nos llevaria a estimaciones incorrectas y más riesgosas.
        Es por eso que el modelo se construyó minimizando los FP dando más importancia a la métrica Precision ¿Pero que es el 
        Precision?

        ### Precision
        Precision = $\frac{TP}{TP+FN}$

        La ecuación de arriba puede explicarse diciendo, de todos los datos que predecimos como positivos
        cuantos son en realidad positivos. así el Precision nos da en términos de porcentaje la cantidad de
        predicciones de la clase positiva que son correctas, incrementar dicha métrica reduce el número de FP.
        """)
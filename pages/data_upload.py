import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
from pre_data import periodos, periodo, deudas, y_max


# @st.cache
def app():
    st.markdown("## Carga de datos")

    # Upload the dataset and save as csv
    st.markdown("### Sube un archivo tipo csv para analizar.")
    st.write("\n")

    # Code to read a single file
    uploaded_file = st.file_uploader("Selecciona un archivo", type=['csv', 'xlsx'])
    global data
    if uploaded_file is not None:
        try:
            data = pd.read_csv(uploaded_file, sep=',')
        except Exception as e:
            print(e)
            data = pd.read_excel(uploaded_file)
    global n_p
    if uploaded_file is not None:
        try:
            # Preprocesado de datos

            #Filtrar columnas
            data = data[(data['desciprcion_uso'] == 'MOTOCICLETAS') | (data['desciprcion_uso'] == 'AUTO PARTICULAR')]

            # buscar la cantidad de periodos dados
            n_p = periodos(data)

            features = ['AVG', 'Inicio', 'valor_', 'persona', 'tarjeta_circulacion',
                        'uso', 'depreciado', 'potencial', 'subsidio', 'tenencia', 'placa']

            cols = []

            for i in range(10):
                cols.append(data.filter(like=features[i], axis=1).columns[0])

            data = data[(cols + n_p + ['placa'])]

            data['tarjeta_circulacion'] = data['tarjeta_circulacion'].replace(np.nan, 'sin tramitar')

            data = data.dropna()

            data['IngresoAVG'] = pd.to_numeric(data['IngresoAVG'])
            data['valor_factura'] = pd.to_numeric(data['valor_factura'])
            data['valor_depreciado_2021'] = pd.to_numeric(data['valor_depreciado_2021'])
            data['Inicio'] = data['Inicio'] + 2000

            # Calcular los periodos pagados
            data['periodos'] = data[data[n_p].columns].apply(periodo, axis=1)

            # Calcular el año actual
            year_max = int('20' + n_p[-1][-2:])
            year_min = int('20' + n_p[0][-2:])

            y = year_max - year_min

            # Calcular la cantidad de deudas
            #data['deuda'] = data[['Inicio', 'periodos']].apply(deudas, axis=1)
            data['deuda'] = (year_max - (data['Inicio'] - 1)) - data['periodos']
            data['deuda'] = pd.to_numeric(data['deuda'])

            data = data[cols + ['deuda', 'placa']]
        except Exception as e:
            print(e)

    # uploaded_files = st.file_uploader("Upload your CSV file here.", type='csv', accept_multiple_files=False)
    # # Check if file exists
    # if uploaded_files:
    #     for file in uploaded_files:
    #         file.seek(0)
    #     uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    #     raw_data = pd.concat(uploaded_data_read)

    # uploaded_files = st.file_uploader("Upload CSV", type="csv", accept_multiple_files=False)
    # print(uploaded_files, type(uploaded_files))
    # if uploaded_files:
    #     for file in uploaded_files:
    #         file.seek(0)
    #     uploaded_data_read = [pd.read_csv(file) for file in uploaded_files]
    #     raw_data = pd.concat(uploaded_data_read)

    # read temp data
    # data = pd.read_csv('data/2015.csv')

    ''' Load the data and save the columns with categories as a dataframe. 
    This section also allows changes in the numerical and categorical columns. '''
    if st.button("Load Data"):

        #data.drop(n_p, axis=1, inplace=True)

        # New data
        st.dataframe(data.head())
        # utils.getProfile(data)
        # st.markdown("<a href='output.html' download target='_blank' > Download profiling report </a>",unsafe_allow_html=True)
        # HtmlFile = open("data/output.html", 'r', encoding='utf-8')
        # source_code = HtmlFile.read()
        # components.iframe("data/output.html")# Save the data to a new file
        data.to_csv('data/main_data.csv', index=False)

        # Generate a pandas profiling report
        # if st.button("Generate an analysis report"):
        #    utils.getProfile(data)
        # Open HTML file

        # 	pass

        # Collect the categorical and numerical columns

        numeric_cols = data.select_dtypes(include=np.number).columns.tolist()
        categorical_cols = list(set(list(data.columns)) - set(numeric_cols))

        # Save the columns as a dataframe or dictionary
        columns = []

        # Iterate through the numerical and categorical columns and save in columns
        columns = utils.genMetaData(data)

        # Save the columns as a dataframe with categories
        # Here column_name is the name of the field and the type is whether it's numerical or categorical
        columns_df = pd.DataFrame(columns, columns=['column_name', 'type'])
        columns_df.to_csv('data/metadata/column_type_desc.csv', index=False)

        # Display columns
        st.markdown("**Column Name**-**Type**")
        for i in range(columns_df.shape[0]):
            st.write(f"{i + 1}. **{columns_df.iloc[i]['column_name']}** - {columns_df.iloc[i]['type']}")

        st.markdown("""Los tipos de columna se encontraron utomaticamente por la aplicacion en los datos. 
        En caso de que quiera cambiar el tipo de dato, ve a la seccion **Cambiar Datos**""")

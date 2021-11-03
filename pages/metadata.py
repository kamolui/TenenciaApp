# Load important libraries
import pandas as pd
import streamlit as st
import os


def app():
    """This application is created to help the user change the metadata for the uploaded file.
    They can perform merges. Change column names and so on.
    """

    # Load the uploaded data
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Por favor sube un archivo en la pagina `Cargar Datos`!")
    else:
        data = pd.read_csv('data/main_data.csv')
        st.dataframe(data)

        # Read the column meta data for this dataset
        col_metadata = pd.read_csv('data/metadata/column_type_desc.csv')

        ''' Change the information about column types
            Here the info of the column types can be changed using dropdowns.
            The page is divided into two columns using beta columns 
        '''
        st.markdown("#### Cambia el tipo de dato en las columnas")

        # Use two column technique
        col1, col2 = st.columns(2)

        global name, type
        # Design column 1
        name = col1.selectbox("Select Column", data.columns)

        # Design column two
        current_type = col_metadata[col_metadata['column_name'] == name]['type'].values[0]
        print(current_type)
        column_options = ['numerical', 'categorical', 'object']
        current_index = column_options.index(current_type)

        type = col2.selectbox("Select Column Type", options=column_options, index=current_index)

        st.write("""Selecciona el nombre de la columna y el tipo de forma.
                    Para aceptar todos los cambios, da click en *Submit changes*""")

        if st.button("Change Column Type"):
            # Set the value in the metadata and resave the file
            # col_metadata = pd.read_csv('data/metadata/column_type_desc.csv')
            st.dataframe(col_metadata[col_metadata['column_name'] == name])

            col_metadata.loc[col_metadata['column_name'] == name, 'type'] = type
            col_metadata.to_csv('data/metadata/column_type_desc.csv', index=False)

            st.write("Se hicieron tus cambios")
            st.dataframe(col_metadata[col_metadata['column_name'] == name])
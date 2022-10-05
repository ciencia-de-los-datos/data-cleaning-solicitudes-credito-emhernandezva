"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df = df.drop('Unnamed: 0',axis=1)
    df = df.dropna()
    
    #mínusculas todos los datos tipo string
    df['sexo'] = df['sexo'].str.lower()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower()
    df['idea_negocio'] = df['idea_negocio'].str.lower()
    df['barrio'] = df['barrio'].str.lower()
    df['línea_credito'] = df['línea_credito'].str.lower()
    
    #eliminar espacios al principio y final
    df['sexo'] = df['sexo'].str.strip()
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.strip()
    df['idea_negocio'] = df['idea_negocio'].str.strip()
    df['barrio'] = df['barrio'].str.strip()
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].str.strip()
    df['línea_credito'] = df['línea_credito'].str.strip()
    
    #reemplazo de caracteres especiales dependiendo de la información de cada columna
    df['idea_negocio'] = df['idea_negocio'].map(lambda x: x.replace('-',' ').replace('_',' ').strip())
    df['barrio'] = df['barrio'].map(lambda x: str(x).replace('-',' ').replace('_',' ').replace('bel¿n','belen').replace('nari¿o','nariño').strip())
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].map(lambda x: str(x).replace('-','/'))
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].map(lambda x: x if len(x.split('/')[0])!=4 else f"{x.split('/')[2]}/{x.split('/')[1]}/{x.split('/')[0]}")
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].map(lambda x: f"{x.split('/')[0].zfill(2)}/{x.split('/')[1].zfill(2)}/{x.split('/')[2].zfill(4)}")
    df['monto_del_credito'] = df['monto_del_credito'].map(lambda x: int(str(x).replace('$','').replace(',','').replace(' ','').replace('.00','')))
    df['línea_credito'] = df['línea_credito'].map(lambda x: x.replace('-','').replace('_','').replace(' ',''))
    df = df.drop_duplicates()
    
    return df

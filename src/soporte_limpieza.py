import pandas as pd

def convertir_columna_a_float(df, columna):
    """
    Esta función reemplaza las comas por puntos en la columna especificada,
    convierte los valores a tipo float.
    
    Parámetros:
    - df: DataFrame en el que se encuentra la columna.
    - columna: El nombre de la columna que se desea convertir.
    
    Retorna:
    - El DataFrame con la columna convertida a tipo float.
    """
    # Reemplazar comas por puntos y convertir a float
    df[columna] = pd.to_numeric(df[columna].str.replace(',', '.', regex=False), errors='coerce')
    
    # Rellenar NaN con 0 (puedes cambiarlo por otro valor si es necesario) y convertir a float
    df[columna] = df[columna].fillna(0).astype(float)
    
    return df


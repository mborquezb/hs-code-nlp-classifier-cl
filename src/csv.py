# src/csv.py
import pandas as pd

def cargar_csv(ruta_archivo):
    import pandas as pd
    """Abre un archivo CSV y lo devuelve como un DataFrame de pandas."""
    try:
        df = pd.read_csv(ruta_archivo)
        print(f"[INFO] Archivo {ruta_archivo} cargado correctamente. Filas: {len(df)}, Columnas: {len(df.columns)}")    
        return df
    except FileNotFoundError:
        print(f"[ERROR] El archivo {ruta_archivo} no se encontró.")
        return None
    except pd.errors.EmptyDataError:
        print(f"[ERROR] El archivo {ruta_archivo} está vacío.")
        return None
    except pd.errors.ParserError:
        print(f"[ERROR] Error al parsear el archivo {ruta_archivo}.")
        return None
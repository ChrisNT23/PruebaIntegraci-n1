import os
import time
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Definir los detalles de la conexión a la base de datos MySQL
configuracion_db = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'database': 'prueba'  # Nombre de la base de datos creada
}

def procesar_archivos_csv(directorio_origen, directorio_respaldo):
    # Conexión a la base de datos MySQL
    conexion = mysql.connector.connect(**configuracion_db)
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost/prueba')

    while True:
        # Obtener la lista de archivos CSV en el directorio de origen
        archivos_csv = [archivo for archivo in os.listdir(directorio_origen) if archivo.endswith('.csv')]
        print("Archivos CSV encontrados:", archivos_csv)
        
        # Procesar cada archivo CSV
        for archivo_csv in archivos_csv:
            ruta_archivo = os.path.join(directorio_origen, archivo_csv)
            
            # Leer el archivo CSV
            datos = pd.read_csv(ruta_archivo)
            
            # Guardar los datos en la base de datos MySQL
            try:
                datos.to_sql('Ventas_Consolidadas', con=engine, if_exists='append', index=False)
                print(f"Datos del archivo {archivo_csv} guardados en la base de datos.")
                
                # Mover el archivo procesado al directorio de respaldo
                os.rename(ruta_archivo, os.path.join(directorio_respaldo, archivo_csv))
                print(f"Archivo {archivo_csv} movido al directorio de respaldo.")
            except Exception as e:
                print(f"Error al procesar el archivo {archivo_csv}: {str(e)}")

        # Esperar un intervalo de tiempo antes de volver a revisar el directorio de origen
        tiempo_espera_segundos = 20  # Esperar 60 segundos antes de revisar nuevamente
        print(f"Esperando {tiempo_espera_segundos} segundos antes de revisar nuevamente...")
        time.sleep(tiempo_espera_segundos)

    # Cerrar la conexión a la base de datos
    conexion.close()

# Directorio de origen y de respaldo
directorio_origen = "C:\\Users\\chris\\Downloads\\origen"
directorio_respaldo = "C:\\Users\\chris\\Downloads\\respaldo"

# Llamar a la función para procesar los archivos CSV
procesar_archivos_csv(directorio_origen, directorio_respaldo)

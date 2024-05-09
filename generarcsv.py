import os
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import shutil

def generar_archivos_csv(directorio_destino):
    try:
        # Crear una instancia de Faker para generar datos ficticios
        fake = Faker()
        
        # Definir el número de registros por archivo CSV
        num_registros = 50

        for i in range(5):  # Generar datos para cada archivo
            # Crear una lista para almacenar los datos generados
            datos = []

            # Generar datos ficticios para cada registro
            for _ in range(num_registros):
                fecha = fake.date_between(start_date='-1y', end_date='today')
                id_local = random.randint(1, 4)  # Supongamos que tienes 4 locales
                id_categoria = random.randint(1, 10)  # Supongamos que tienes 10 categorías
                id_producto = random.randint(1, 100)  # Supongamos que tienes 100 productos
                cantidad = random.randint(1, 20)
                precio_unitario = round(random.uniform(10, 100), 2)
                total_venta = round(cantidad * precio_unitario, 2)

                datos.append([id_local, fecha, id_categoria, id_producto, cantidad, precio_unitario, total_venta])

            # Crear un DataFrame con los datos
            df = pd.DataFrame(datos, columns=['IdLocal', 'Fecha', 'IdCategoria', 'IdProducto', 'Cantidad', 'PrecioUnitario', 'TotalVenta'])

            # Crear el archivo CSV en el directorio de destino
            archivo_csv = os.path.join(directorio_destino, f'reporte_ventas_{i + 1}.csv')
            df.to_csv(archivo_csv, index=False)

        print("Archivos CSV generados exitosamente.")
        
        # Llamar a la función para descargar los archivos
        descargar_archivos_csv(directorio_destino)
        
    except Exception as e:
        print("Error al generar archivos CSV:", str(e))

def descargar_archivos_csv(directorio_destino):
    try:
        # Verificar si el directorio de destino existe, si no, crearlo
        if not os.path.exists(directorio_destino):
            os.makedirs(directorio_destino)
        
        # Mover los archivos CSV generados al directorio de destino
        for i in range(10):
            nombre_archivo = f'reporte_ventas_{i + 1}.csv'
            shutil.copy(nombre_archivo, os.path.join(directorio_destino, nombre_archivo))
        
        print("Archivos CSV descargados exitosamente en el directorio:", directorio_destino)
    except Exception as e:
        print("Error al descargar archivos CSV:", str(e))

# Llamar a la función para generar y descargar los archivos CSV
directorio_destino = "C:\\Users\\chris\\Downloads\\origen"  # Cambiar por el directorio donde deseas descargar los archivos
generar_archivos_csv(directorio_destino)

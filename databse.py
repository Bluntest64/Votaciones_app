import mysql.connector
from config import Config
from mysql.connector import Error

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB,
            port=Config.MYSQL_PORT
        )
        if conexion.is_connected():
            print("Conexión a MySQL exitosa")
            return conexion
    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
        raise ConnectionError(f"No se pudo conectar a la base de datos: {e}")
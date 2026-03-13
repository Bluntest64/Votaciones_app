CREATE DATABASE votaciones_db;
use votaciones_db;

CREATE TABLE ciudadanos (
id INT auto_increment primary key, 
documento varchar(20), 
nombre varchar(1009), 
ciudad varchar(100), 
telefono varchar(20)
);

CREATE TABLE puestos_votacion (

id INT AUTO_INCREMENT PRIMARY KEY,
documento VARCHAR(20),
lugar VARCHAR(100),
direccion VARCHAR(100),
mesa INT

);

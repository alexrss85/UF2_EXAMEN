import psycopg2 as psy
from connection import conexio

conn=conexio()


def afegirUsuari(conn,nombre,apellido,correoElectronico,descripcion,curso,ano,direccion,codigoPostal,password):
    


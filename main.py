from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from connection import conexio
from add_user import afegirUsuari
import user_schema

conn = conexio()

app = FastAPI()

# EXERCICI 1

class User(BaseModel):
    nombre: str    # Alex
    apellido: str   # Rosendo
    correoElectronico: str  # a@gmail.com
    descripcion: str | None = None # hola
    curso: str  # DAW
    ano: int    # 2
    direccion: str  # Carrer itic
    codigoPostal: int | None = None #11111111
    password: str   #12345Ab


# EXERCICI 2

@app.post("/users/")
async def create_item(user: User):
    try:
        afegirUsuari(conn, user.nombre, user.apellido, user.correoElectronico, user.descripcion,user.curso, user.ano, user.direccion, user.codigoPostal, user.password)
    except Exception (e):
        print ("error:  {e}")
    finally:
        conn.close()


# EXERCICI 4 

@app.get(path="/users", response_model=List[dict])
async def read_user():
    return user_schema.users_schema(read_user(conn))
    






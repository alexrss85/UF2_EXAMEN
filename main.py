from fastapi import FastAPI
from pydantic import BaseModel
from connection import conexio

conn = conexio()

app = FastAPI()


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

async def add_user(nombre: str, apellido: str, correoElectronico: int, descripcion: str, curso: str,):
  
    






from ninja import Schema

class UsuarioSchema(Schema):
    id: int
    nombre: str
    apaterno: str
    amaterno: str
    edad: int
    nomcuenta: str

class UsuarioCreateSchema(Schema):
    nombre: str
    apaterno: str
    amaterno: str
    edad: int
    nomcuenta: str
    password: str
    
    
class UsuarioUpdateSchema(Schema):
    nombre: str = None
    apaterno: str = None
    amaterno: str = None
    edad: int = None
    nomcuenta: str = None
    password: str = None
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base= declarative_base()

class Profesor(Base):
    __tablename__ = 'Profesor'

    ProfesorId= Column(Integer(), primary_key=True, autoincrement=True)
    Nombre= Column(String(60), nullable= False)
    Apellido= Column(String(60), nullable= False)
    Documento= Column(String(10), nullable= False, unique=True)
    Legajo= Column(String(10), nullable= False, unique=True)
    Apodo= Column(String(120), nullable= True)
    TituloId= Column(Integer, nullable= False, unique=True)


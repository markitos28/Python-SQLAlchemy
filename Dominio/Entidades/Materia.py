from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base= declarative_base()

class Materia(Base):
    __tablename__ = 'Materia'

    MateriaId= Column(Integer(), primary_key=True, autoincrement=True)
    MateriaDesc= Column(String(120), nullable= False, unique=True)
    FechaMateriaAlta= Column(DateTime(), default=datetime.now(), nullable= False)
    FechaMateriaBaja= Column(DateTime(), default=datetime.now(), nullable= True)


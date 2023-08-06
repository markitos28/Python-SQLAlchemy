from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base= declarative_base()

class ProfesorMateria(Base):
    __tablename__ = 'ProfesorMateria'

    ProfesorMateriaId= Column(Integer(), primary_key=True, autoincrement=True)
    ProfesorId= Column(Integer(), nullable= False, unique=True)
    MateriaId= Column(Integer(), nullable= False, unique=True)


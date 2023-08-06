# Contendrá el inicio de la aplicacion con la definicion e inyeccion de dependencias
import sys
sys.path.insert(1,'../Infraestructura/Querys')
import MateriaQuery

obj = MateriaQuery()
query= obj.SelectAllMateria()

print(query)




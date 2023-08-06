from sqlalchemy import select
from Contextos.SqlServerContext import SessionSQLServer
from Dominio.Entidades import Materia

class MateriaQuery():
    session= SessionSQLServer()
    
    def SelectAllMateria(self):
        query = select(Materia)
        selectAll= self.session.scalars(query)
        return selectAll

    def SelectIdMateria(self, materiaId):
        query= select(Materia).where(Materia.MateriaId == materiaId)
        select = self.session.scalars(query).one()
        return select
    
    def SelectLikeDescMateria(self, descripcion):
        query = select(Materia).where(Materia.MateriaDesc.like('%' + descripcion + '%'))
        selectLike= self.session.scalars(query)
        return selectLike

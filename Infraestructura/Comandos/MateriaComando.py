from Contextos.SqlServerContext import SessionSQLServer
class MateriaComando():
    session= SessionSQLServer()
    
    def InsertMateria(self, materia):
        self.session.add(materia)
        self.session.commit()

    def DeleteMateria(self, materia):
        self.session.delete(materia)
        self.session.commit()

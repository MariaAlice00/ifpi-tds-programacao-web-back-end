from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioSerie():
    def __init__(self, db: Session): # db do tipo Session
        self.db = db


    def criar(self, serie: schemas.Serie):
        db_serie = models.Serie(titulo=serie.titulo, ano=serie.ano, genero=serie.genero, qtd_temporadas=serie.qtd_temporadas)

        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)

        return db_serie


    def listar(self):
        series = self.db.query(models.Serie).all() # query: consultar

        return series


    def exibir_id(self, id):
        lista_id = self.db.query(models.Serie).filter(models.Serie.id == id).first()
        '''stmt = select(model.Serie).filter_by(id=id)
           serie = self.db.execute(stmt).one()'''
        
        return lista_id


    def exibir_titulo(self, titulo):
        lista_titulo = self.db.query(models.Serie).filter(models.Serie.titulo == titulo).first()
        return lista_titulo


    def remover(self, id):
        lista_remover = self.db.query(models.Serie).filter(models.Serie.id == id).first()
        
        self.db.delete(lista_remover)
        self.db.commit()

        return 'Série removida'
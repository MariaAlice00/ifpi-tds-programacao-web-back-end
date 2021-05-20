from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario():
    def __init__(self, session: Session):
        self.session = session

    
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(nome=usuario.nome, 
                                    senha=usuario.senha, 
                                    telefone=usuario.telefone)

        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)

        return db_usuario

    
    def listar(self):
        stmt = select(models.Usuario)
        usuarios = self.session.execute(stmt).scalars().all()
        #usuarios = self.db.query(models.Usuario).all()

        return usuarios

    
    def obter():
        pass


    def remover():
        pass
from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto():
    def __init__(self, db: Session): # db do tipo Session
        self.db = db


    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(nome=produto.nome, detalhes=produto.detalhes, preco=produto.preco, disponivel=produto.disponivel, tamanhos=produto.tamanhos, usuario_id=produto.usuario_id)

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto


    def listar(self):
        produtos = self.db.query(models.Produto).all() # query: consultar
        return produtos


    def obter(self, id):
        produtos_id = self.db.query(models.Produto).filter(models.Produto.id == id).first()
        return produtos_id


    def remover(self):
        pass



class RepositorioUsuario():
    def __init__(self, db: Session): # db do tipo Session
        self.db = db

    #id, nome, telefone
    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Produto(nome=usuario.nome, telefone=usuario.telefone)

        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario


    def listar(self):
        usuarios = self.db.query(models.Usuario).all() # query: consultar
        return usuarios

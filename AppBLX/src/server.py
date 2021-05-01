from fastapi import FastAPI, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto


criar_bd()


app = FastAPI()


@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)

    return produto_criado


@app.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[Produto])
def listar_produtos(db: Session = Depends(get_db)):
    produtos  = RepositorioProduto(db).listar()
    return produtos


@app.get('/produtos/{id}', status_code=status.HTTP_200_OK, response_model=List[Produto])
def obter_produtos(db: Session = Depends(get_db)):
    produtos_id = RepositorioProduto(db).obter(id)
    return produtos_id
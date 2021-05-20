from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto, ProdutoSimples
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto


router = APIRouter()


@router.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@router.get('/produtos', status_code=status.HTTP_200_OK, response_model=List[ProdutoSimples])
def listar_produtos(db: Session = Depends(get_db)):
    produtos  = RepositorioProduto(db).listar()
    return produtos


@router.get('/produtos/{id}')
def exibir_produto(id: int, db: Session = Depends(get_db)):
    produto_localizado = RepositorioProduto(db).buscarPorId(id)

    if not produto_localizado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não há um produto com o id = {id}')

    return produto_localizado


@router.put('/produtos/{id}', status_code=status.HTTP_200_OK, response_model=ProdutoSimples)
def editar_produto(id: int, produto: Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(id, produto)
    produto.id = id
    return produto


@router.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return {"msg": "produto removido com sucesso"}


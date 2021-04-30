from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Serie
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.serie import RepositorioSerie


criar_bd()


app = FastAPI()


@app.post('/series')
def criar_serie(serie: Serie, db: Session = Depends(get_db)):
    serie_criada = RepositorioSerie(db).criar(serie)
    return serie_criada


@app.get('/series')
def listar_series(db: Session = Depends(get_db)):
    series  = RepositorioSerie(db).listar()
    return series


@app.get('/series/{id}')
def listar_id(id: int, db: Session = Depends(get_db)):
    series_id = RepositorioSerie(db).exibir_id(id)
    return series_id
    # se o id não existe, retorna null


@app.put('/series/{titulo}')
def listar_titulo(titulo: str, db: Session = Depends(get_db)):
    series_titulo = RepositorioSerie(db).exibir_titulo(titulo)
    return series_titulo


@app.delete('/series/{id}')
def remover_serie(id: int, db: Session = Depends(get_db)):
    series_removidas = RepositorioSerie(db).remover(id)
    return series_removidas
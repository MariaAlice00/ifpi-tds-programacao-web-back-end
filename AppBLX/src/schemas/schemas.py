from pydantic import BaseModel
from typing import Optional, List


class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    telefone: str
    #produtos: List[produtos] = []
    tamanhos: str
    usuario_id: str

    class Config:
        orm_mode = True


class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class Config:
        orm_mode = True


class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    entrega: bool = True
    observacoes: Optional[str] = 'Sem observações'
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[int]
    nome: str
    idade: int
    sexo: str
    cor: str

# criar o banco de dados
banco: List[Animal] = []


@app.get('/animais')
def listar_animais():
    return banco


@app.post('/animais')
def criar_animal(animal: Animal):
    animal.id = str(uuid4()) # sortear o id
    banco.append(animal)
    return {'mensagem': 'Animal cadastrado com sucesso.'}


@app.get('/animais/{id}')
def encontrar_animal(id: str):
    for animal in banco:
        if animal.id == id:
            return animal
    return {'erro': 'Animal não encontrado.'}


@app.delete('/animais/{id}')
def apagar_animal(id: str):
    posicao = -1
    for index, animal in enumerate(banco): # index: posição, animal: objeto
        if animal.id == id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'mensagem': 'Animal removido com sucesso!'}
    else:
        return {'erro': 'Animal não encontrado.'}
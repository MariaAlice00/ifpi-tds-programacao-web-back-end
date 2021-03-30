from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Path parameters
@app.get("/saudacao/{nome}") # na hora de digitar na url coloque /saudacao/nome qualquer
def saudacao(nome:str):
    texto = f'Olá {nome}, tudo em paz?!'
    return {"mensagem":texto}

@app.get("/quadrado/{numero}")
def quadrado(numero:int):
    resultado = numero * numero
    texto = f'O quadrado de {numero} é {resultado}'
    return {"mensagem": texto}

# Query parameters
@app.get("/dobro") # na hora de digitar na url coloque /dobro?valor=número qualquer
def dobro(valor:int):
    resultado = valor * 2
    return {"resultado": f'O dobro de {valor} é {resultado}'}

@app.get("/area-retangulo") # /area-retangulo?largura=5&altura=6
def area_retangulo(largura:int, altura: int=2): # pode atribuir valor a altura por exemplo: altura: int = 2, só será 2 se não mandar o valor da altura
    area = largura * altura
    return {"area": area}


# Request body (enviar); método POST

class Produto(BaseModel):
    nome: str
    preco: float

@app.post('/produtos')
def produtos(produto: Produto):
    return {"mensagem": f"Produto ({produto.nome} - R$ {produto.preco}) cadastrado com sucesso!"}
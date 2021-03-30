from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World!!!"}


@app.get("/profile")
def profile():
    return {"name": "Maria Alice"}


@app.post('/profile')
def signup():
    return {"message: Perfil criado com sucesso!"}


@app.put('/profile')
def atualizar():
    return {"message: Perfil atualizado com sucesso!"}


@app.delete('/profile')
def remover():
    return {"message: Perfil removido com sucesso!"}
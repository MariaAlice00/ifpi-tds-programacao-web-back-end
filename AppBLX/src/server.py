from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_produtos, rotas_usuarios, rotas_pedidos

app = FastAPI()

#CORS
origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rotas PRODUTOS
app.include_router(rotas_produtos.router) # incluir os arquivos de rota

# Rotas USUÁRIOS
app.include_router(rotas_usuarios.router) 

# Rotas PEDIDOS
app.include_router(rotas_pedidos.router)
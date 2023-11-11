from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_routes

app = FastAPI()

app.include_router(
    user_routes.user_router,
    prefix="/user"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"message":"hello"}
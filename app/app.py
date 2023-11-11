from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import user_routes
from profile import profile_routes

app = FastAPI()

app.include_router(
    user_routes.user_router,
    prefix="/user",
    
     
)
app.include_router(
    profile_routes.profile_router,
    prefix="/profile",
    
     
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
from fastapi import APIRouter, HTTPException, Depends, status
from controllers import user_controller
from middleware.middleware import create_token, encode_token
from fastapi.security import OAuth2PasswordBearer

user_router = APIRouter()

user_repo = user_controller.UserController(
    "mongodb://admin:T3sT_s3rV@nik.ydns.eu:400/"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@user_router.post("/")
async def create_user(request: user_controller.User):
    response = await user_repo.create_user(request)
    if not response:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "user not create"
        )
    return {"response": f"inserted id {response}"}

@user_router.post("/login")
async def login(request: user_controller.User):
    user = await user_repo.get_user_by_username(request.username)
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "user not excist"
        )
    token = create_token({
        "id":user
    })
    return {"accsess_token": token}

@user_router.get("/me")
async def getMe(token: str = Depends(oauth2_scheme)):
    payload = encode_token(token)
    user = await user_repo.get_user(payload["id"])
    if not user:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "user not found"
        )
    return user
    
    
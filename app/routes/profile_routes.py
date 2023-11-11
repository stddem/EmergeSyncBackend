from fastapi import APIRouter, HTTPException, Depends, status
from controllers import profile_controller
from middleware.middleware import create_token, encode_token
from fastapi.security import OAuth2PasswordBearer

profile_router = APIRouter()


profile_repo = profile_controller.ProfileController(
    "mongodb://admin:T3sT_s3rV@nik.ydns.eu:400/"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@profile_router.post("/")
async def create_profile(request: profile_controller.Profile):
    response = await profile_repo.create_profile(request)
    if not response:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "user not create"
        )
    return {"response": f"inserted id {response}"}

@profile_router.get("/")
async def get(token: str = Depends(oauth2_scheme)):
    payload = encode_token(token) 
    profile = await profile_repo.get_profile(payload["id"])
    if not profile:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            "user not found"
        )
    return profile





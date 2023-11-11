from fastapi import APIRouter, HTTPException, Depends, status
from controllers import profile_controller
from middleware.middleware import create_token, encode_token
from fastapi.security import OAuth2PasswordBearer

profile_router = APIRouter()

profile_repo = profile_controller.ProfileController(
    "mongodb://admin:T3sT_s3rV@nik.ydns.eu:400/"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")







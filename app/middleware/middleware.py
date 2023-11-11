import jwt

def create_token(payload:dict) -> str:
    token = jwt.encode(
        payload= payload,
        key= "SECRET"
    )
    return token

def encode_token(token:str) -> dict:
    pyload = jwt.decode(
        jwt=token,
        key="SECRET",
        algorithms="HS256"
    )
    return pyload
from database import Database
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


def api_key_auth(
    api_key: str = Depends(OAuth2PasswordBearer(tokenUrl='token')),
):
    api_keys = [
        record['value']
        for record in Database.users_api_keys_collection.find({})
    ]

    if api_key not in api_keys:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail='Forbidden'
        )

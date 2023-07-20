from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.schema.auth import TokenReturn
from jose import jwt

JWT_SECRET_KEY = 'thisisescretkey'

oauth2_schema = OAuth2PasswordBearer(tokenUrl='api/auth/login')

router = APIRouter(prefix='/api/auth', tags=['auth'])


async def verify_token(token: str = Depends(oauth2_schema)):
    try:
        jwt.decode(token, JWT_SECRET_KEY)
    except:
        raise HTTPException(status_code=401)


@router.post('/login', response_model=TokenReturn)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == 'admin' and form_data.password == '123456':
        return {
            'access_token': jwt.encode(
                {'username': form_data.username},
                JWT_SECRET_KEY
            ),
            'token_type': 'bearer'
        }
    raise HTTPException(status_code=404)

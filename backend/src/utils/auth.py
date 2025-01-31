from base64 import b64decode
import datetime
from pprint import pprint
from fastapi import HTTPException
import bcrypt
import jwt
from jwt.exceptions import InvalidTokenError
from backend.src.db.db_util import getCursor
from backend.src.utils.ConfigUtils import ConfigUtils
from backend.src.utils.exception_decorators import jwt_exception_handler


def hash(password:str) -> str:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password,salt)



def encode_auth_token(user_email) -> str:
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'sub': user_email
        }
   
        token = jwt.encode(payload, ConfigUtils.jwt_secret, algorithm="HS256")
        pprint(token)
        return token
    except Exception as e:
        return e

#@jwt_exception_handler
def getUserEmailFromJwt(jwt_token:str):
    if(jwt_token == None):
        raise HTTPException(status_code=401,detail="Did not Provide Bearer JWT Token")
    if( jwt_token.startswith("Bearer ") == False):
        raise HTTPException(status_code=401, detail="Bearer token value does not begin with 'Bearer '")
        
    jwt_token = jwt_token[7:]
    dict = jwt.decode(jwt_token, ConfigUtils.jwt_secret, algorithms=['HS256'] )
    email = dict["sub"]
    print(type(dict["sub"]))
    print(email)
    return email





import hashlib
import hmac

def get_hashed_password(plane_password:str)->str:
    return hashlib.sha256(plane_password.encode('utf-8')).hexdigest()

def verify_hashed_password(plane_password:str,hashed_password:str)-> bool:
    verify = get_hashed_password(plane_password)
    return hmac.compare_digest(verify,hashed_password)
from sqlalchemy.orm import Session
from db.models import AI

def create_prompt(user_id:int,user_prompt:str,ai_response:str,db:Session):
    user_input = AI(user_id=user_id,user_prompt=user_prompt,ai_response=ai_response)
    db.add(user_input)
    db.commit()
    return user_input
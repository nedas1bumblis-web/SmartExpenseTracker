from fastapi import APIRouter,HTTPException,Depends,Request
from sqlalchemy.orm import Session
from schemas import AIQuery
from services.ai_service import ai_creation
from db.session import get_db
router = APIRouter()

@router.post('/AI')
async def ai_route(ai:AIQuery,request:Request,db:Session = Depends(get_db)):
    client = request.app.state.client
    ai_logic = await ai_creation(ai,client,db)
    return ai_logic

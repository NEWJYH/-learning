from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import schemas, models, database
from hashing import Hash
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    # email 확인 작업
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Invalid Credentials")
    # 비밀번호 토큰 jwt 확인작업
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Incorrect password")
    #generate a jwt token and return 
    return user


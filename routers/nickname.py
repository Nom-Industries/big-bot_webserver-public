from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from fastapi.responses import JSONResponse
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_delete, crud_patch

from typing import List

import utils

router = APIRouter(
    prefix="/nickname",
    tags=["Nicknames"]
)

@router.get("/config", response_model=List[schemas.NicknameMainBase])
def get_nickname(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_nickname_main(db, request.query_params._dict))

@router.post("/config", response_model=schemas.NicknameMainBase)
def create_nickname(nickname: schemas.NicknameMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_nickname_main(db, {"channel_id", nickname.channel_id}))
    
    return crud_post.insert_nickname_config(db, nickname)

@router.patch("/config", response_model=schemas.NicknameMainBase)
def update_nickname(nickname: schemas.NicknameMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_nickname = crud_get.get_nickname_main(db, {"channel_id", nickname.channel_id})[0]

    utils.check_if_exists(db_nickname, modifying=True)
    
    return crud_patch.update_nickname_config(db, old_nickname=db_nickname, new_nickname=nickname)

@router.delete("/config", status_code=204)
def delete_nickname(nickname: schemas.NicknameMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_nickname = crud_get.get_nickname_main(db, {"channel_id", nickname.channel_id})[0]

    utils.check_if_exists(db_nickname, modifying=True)

    crud_delete.delete_nickname_main(db, db_nickname)

@router.get("/request", response_model=List[schemas.NicknameRequestsBase])
def get_nickname_requests(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_nickname_requests(db, request.query_params._dict))

@router.post("/request", response_model=schemas.NicknameRequestsBase)
def create_nickname_requests(nickname_request: schemas.NicknameRequestsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_nickname_requests(db, {"message_id", nickname_request.message_id}))
    
    return crud_post.insert_nickname_request(db, nickname_request)

@router.patch("/request", response_model=schemas.NicknameRequestsBase)
def update_nickname_requests(nickname_request: schemas.NicknameRequestsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_nickname_request = crud_get.get_nickname_requests(db, {"message_id", nickname_request.message_id})[0]

    utils.check_if_exists(db_nickname_request, modifying=True)
    
    return crud_patch.update_nickname_request(db, old_nickname_request=db_nickname_request, new_nickname_request=nickname_request)

@router.delete("/request", status_code=204)
def delete_nickname_requests(nickname_request: schemas.NicknameRequestsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_nickname_request = crud_get.get_nickname_requests(db, {"message_id", nickname_request.message_id})[0]

    utils.check_if_exists(db_nickname_request, modifying=True)

    crud_delete.delete_nickname_request(db, db_nickname_request)
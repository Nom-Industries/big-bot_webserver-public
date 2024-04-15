from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/sticky_messages",
    tags=["Sticky Messages"]
)

@router.get("/", response_model=List[schemas.StickyMainBase])
def get_sticky_messages(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_sticky_message_info(db, request.query_params._dict))

@router.post("/", response_model=schemas.StickyMainBase, status_code=201)
def create_sticky_message(sticky_message: schemas.StickyMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_sticky_message_info(db, {"channel_id": sticky_message.channel_id}))

    return crud_post.insert_sticky_message(db, sticky_message)

@router.patch("/", response_model=schemas.StickyMainBase)
def update_sticky_message(sticky_message: schemas.StickyMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_sticky_message = crud_get.get_sticky_message_info(db, {"channel_id": sticky_message.channel_id})[0]

    utils.check_if_exists(db_sticky_message, modifying=True)
    
    return crud_patch.update_sticky_message_detail(db, old_sticky_message=db_sticky_message, new_sticky_message=sticky_message)

@router.delete("/", status_code=204)
def delete_sticky_message(sticky_message: schemas.StickyMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_sticky_message = crud_get.get_sticky_message_info(db, {"channel_id": sticky_message.channel_id})[0]

    utils.check_if_exists(db_sticky_message, modifying=True)

    crud_delete.delete_sticky_message_detail(db, db_sticky_message)
from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/auto_threads",
    tags=["Auto Threads"]
)

@router.get("/", response_model=List[schemas.AutoThreadMainBase])
def get_auto_thread_config(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_auto_thread_info(db, request.query_params._dict))

@router.post("/", response_model=schemas.AutoThreadMainBase, status_code=201)
def create_auto_thread(auto_thread: schemas.AutoThreadMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_auto_thread_info(db, {"channel_id": auto_thread.channel_id}))

    return crud_post.insert_auto_thread(db, auto_thread)

@router.patch("/", response_model=schemas.AutoThreadMainBase)
def update_auto_thread(auto_thread: schemas.AutoThreadMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_auto_thread = crud_get.get_auto_thread_info(db, {"channel_id": auto_thread.channel_id})[0]

    utils.check_if_exists(db_auto_thread, modifying=True)
    
    return crud_patch.update_auto_thread_detail(db, old_auto_thread=db_auto_thread, new_auto_thread=auto_thread)

@router.delete("/", status_code=204)
def delete_auto_thread(auto_thread: schemas.AutoThreadMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_auto_thread = crud_get.get_auto_thread_info(db, {"channel_id": auto_thread.channel_id})[0]

    utils.check_if_exists(db_auto_thread, modifying=True)

    crud_delete.delete_auto_thread_detail(db, db_auto_thread)
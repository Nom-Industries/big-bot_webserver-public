from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/autopublish",
    tags=["Autopublish"]
)

@router.get("/", response_model=List[schemas.AutopublishBase])
def get_autopublish_channels_config(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_autopublish_channels(db, request.query_params._dict))

@router.post("/", response_model=schemas.AutopublishBase, status_code=201)
def create_autopublish_channels(autopublish_channels: schemas.AutopublishBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_autopublish_channels(db, {"channel_id": autopublish_channels.channel_id}))

    return crud_post.insert_autopublish_channels(db, autopublish_channels)

@router.patch("/", response_model=schemas.AutopublishBase)
def update_autopublish_channels(autopublish_channels: schemas.AutopublishBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_autopublish_channel = crud_get.get_autopublish_channels(db, {"channel_id": autopublish_channels.channel_id})[0]

    utils.check_if_exists(db_autopublish_channel, modifying=True)
    
    return crud_patch.update_autopublish_channels(db, old_autopublish=db_autopublish_channel, new_autopublish=autopublish_channels)

@router.delete("/", status_code=204)
def delete_autopublish_channels(autopublish_channels: schemas.AutopublishBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_autopublish_channel = crud_get.get_autopublish_channels(db, {"channel_id": autopublish_channels.channel_id})[0]

    utils.check_if_exists(db_autopublish_channel, modifying=True)

    crud_delete.delete_autopublish_channels(db, db_autopublish_channel)
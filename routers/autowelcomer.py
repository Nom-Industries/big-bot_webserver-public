from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/autowelcomer",
    tags=["Autowelcomer"]
)

@router.get("/", response_model=List[schemas.AutowelcomerBase])
def get_autowelcomer_channels_config(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_autowelcomer_channels(db, request.query_params._dict))

@router.post("/", response_model=schemas.AutowelcomerBase, status_code=201)
def create_autowelcomer_channels(autowelcomer_channels: schemas.AutowelcomerBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_autowelcomer_channels(db, {"channel_id": autowelcomer_channels.channel_id}))

    return crud_post.insert_autowelcomer_channels(db, autowelcomer_channels)

@router.patch("/", response_model=schemas.AutowelcomerBase)
def update_autowelcomer_channels(autowelcomer_channels: schemas.AutowelcomerBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_autowelcomer_channel = crud_get.get_autowelcomer_channels(db, {"channel_id": autowelcomer_channels.channel_id})[0]

    utils.check_if_exists(db_autowelcomer_channel, modifying=True)
    
    return crud_patch.update_autowelcomer_channels(db, old_autowelcomer=db_autowelcomer_channel, new_autowelcomer=autowelcomer_channels)

@router.delete("/", status_code=204)
def delete_autowelcomer_channels(autowelcomer_channels: schemas.AutowelcomerBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_autowelcomer_channel = crud_get.get_autowelcomer_channels(db, {"channel_id": autowelcomer_channels.channel_id})[0]

    utils.check_if_exists(db_autowelcomer_channel, modifying=True)

    crud_delete.delete_autowelcomer_channels(db, db_autowelcomer_channel)
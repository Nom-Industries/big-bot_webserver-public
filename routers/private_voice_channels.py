from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/private_voice",
    tags=["Private Voice Channels"]
)

@router.get("/channels", response_model=List[schemas.VoiceChannelsBase])
def get_private_voice_channels(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_priv_voice_channels(db, request.query_params._dict))

@router.post("/channels", response_model=schemas.VoiceChannelsBase, status_code=201)
def create_private_voice_channel(channel: schemas.VoiceChannelsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_priv_voice_channels(db, {"channel_id": channel.channel_id}))

    return crud_post.insert_private_voice_channel(db, channel)

@router.patch("/channels", response_model=schemas.VoiceChannelsBase)
def update_private_voice_channel(channel: schemas.VoiceChannelsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_channel = crud_get.get_priv_voice_channels(db, {"channel_id": channel.channel_id})[0]

    utils.check_if_exists(db_channel, modifying=True)
    
    return crud_patch.update_private_voice_channel_detail(db, old_channel=db_channel, new_channel=channel)

@router.delete("/channels", status_code=204)
def delete_private_voice_channel(channel: schemas.VoiceChannelsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_channel = crud_get.get_priv_voice_channels(db, {"channel_id": channel.channel_id})[0]

    utils.check_if_exists(db_channel, modifying=True)

    crud_delete.delete_private_voice_channel_detail(db, db_channel)

@router.get("/config", response_model=List[schemas.VoiceChannelsMainBase])
def get_private_voice_channel_config(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_priv_voice_channel_config(db, request.query_params._dict))

@router.post("/config", response_model=schemas.VoiceChannelsMainBase, status_code=201)
def create_private_voice_channel_config(channel: schemas.VoiceChannelsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_priv_voice_channel_config(db, {"channel_id": channel.channel_id}))

    return crud_post.insert_private_voice_channel_config(db, channel)

@router.patch("/config", response_model=schemas.VoiceChannelsMainBase)
def update_private_voice_channel_config(channel: schemas.VoiceChannelsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_channel = crud_get.get_priv_voice_channel_config(db, {"channel_id": channel.channel_id})[0]

    utils.check_if_exists(db_channel, modifying=True)
    
    return crud_patch.update_private_voice_channel_config_detail(db, old_channel=db_channel, new_channel=channel)

@router.delete("/config", status_code=204)
def delete_private_voice_channel_config(channel: schemas.VoiceChannelsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_channel = crud_get.get_priv_voice_channel_config(db, {"channel_id": channel.channel_id})[0]

    utils.check_if_exists(db_channel, modifying=True)

    crud_delete.delete_private_voice_channel_config_detail(db, db_channel)
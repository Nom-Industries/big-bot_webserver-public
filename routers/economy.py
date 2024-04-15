from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/economy",
    tags=["Economy"]
)

@router.get("/", response_model=List[schemas.EconomyMainBase])
def get_economy(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_economy_info(db, request.query_params._dict))

@router.post("/", response_model=schemas.EconomyMainBase, status_code=201)
def create_economy_player(user: schemas.EconomyMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_economy_info(db, {"user_id": user.user_id}))

    return crud_post.insert_economy_player(db, user)

@router.patch("/", response_model=schemas.EconomyMainBase)
def update_economy_player(user: schemas.EconomyMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_user = crud_get.get_economy_info(db, {"user_id": user.user_id})[0]

    utils.check_if_exists(db_user, modifying=True)
    
    return crud_patch.update_economy_player_detail(db, old_user=db_user, new_user=user)

@router.delete("/", status_code=204)
def delete_economy_player(user: schemas.EconomyMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_user = crud_get.get_economy_info(db, {"user_id": user.user_id})[0]

    utils.check_if_exists(db_user, modifying=True)

    return crud_delete.delete_economy_user_detail(db, db_user)

@router.get("/settings", response_model=List[schemas.Economy_User_SettingsBase])
def get_economy_settings(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_economy_user_settings(db, request.query_params._dict))

@router.post("/settings", response_model=schemas.Economy_User_SettingsBase, status_code=201)
def create_economy_settings(user: schemas.Economy_User_SettingsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_economy_user_settings(db, {"user": user.user}))

    return crud_post.insert_economy_user_settings(db, user)

@router.patch("/settings", response_model=schemas.Economy_User_SettingsBase)
def update_economy_settings(user: schemas.Economy_User_SettingsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_user = crud_get.get_economy_user_settings(db, {"user": user.user})[0]

    utils.check_if_exists(db_user, modifying=True)
    
    return crud_patch.update_economy_user_settings(db, old_economy_user=db_user, new_economy_user=user)

@router.delete("/settings", status_code=204)
def delete_economy_settings(user: schemas.Economy_User_SettingsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_user = crud_get.get_economy_user_settings(db, {"user": user.user})[0]

    utils.check_if_exists(db_user, modifying=True)

    return crud_delete.delete_economy_user_settings(db, db_user)
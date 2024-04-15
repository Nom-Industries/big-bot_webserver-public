from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/user_statistics",
    tags=["User Statistics"]
)

@router.get("/", response_model=List[schemas.UserStatisticsBase])
def get_user_statistics(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_user_statistics(db, request.query_params._dict))

@router.post("/", response_model=schemas.UserStatisticsBase, status_code=201)
def create_user_statistics(user_statistics: schemas.UserStatisticsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_user_statistics(db, {"unique_id": f"{user_statistics.guild_id}-{user_statistics.user_id}"}))

    return crud_post.insert_user_statistics(db, user_statistics)

@router.patch("/", response_model=schemas.UserStatisticsBase)
def update_user_statistics(user_statistics: schemas.UserStatisticsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_user_statistics = crud_get.get_user_statistics(db, {"unique_id": f"{user_statistics.guild_id}-{user_statistics.user_id}"})[0]

    utils.check_if_exists(db_user_statistics, modifying=True)
    
    return crud_patch.update_user_statistics(db, old_user_stats=db_user_statistics, new_user_stats=user_statistics)

@router.delete("/", status_code=204)
def delete_user_statistics(user_statistics: schemas.UserStatisticsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_user_statistics = crud_get.get_user_statistics(db, {"unique_id": f"{user_statistics.guild_id}-{user_statistics.user_id}"})[0]

    utils.check_if_exists(db_user_statistics, modifying=True)

    crud_delete.delete_user_statistics(db, db_user_statistics)
from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/notifications",
    tags=["Notifications"]
)

@router.get("/", response_model=List[schemas.NotificationsBase])
def get_notifications(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_notifications(db, request.query_params._dict))

@router.post("/", response_model=schemas.NotificationsBase, status_code=201)
def create_notifications(notification: schemas.NotificationsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_notifications(db, {"channel_id": notification.channel_id}))

    return crud_post.insert_notifications(db, notification)

@router.patch("/", response_model=schemas.NotificationsBase)
def update_notifications(notification: schemas.NotificationsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_notification = crud_get.get_notifications(db, {"channel_id": notification.channel_id})[0]

    utils.check_if_exists(db_notification, modifying=True)
    
    return crud_patch.update_notifications(db, old_notifications=db_notification, new_notifications=notification)

@router.delete("/", status_code=204)
def delete_notifications(notification: schemas.NotificationsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_notification = crud_get.get_notifications(db, {"channel_id": notification.channel_id})[0]

    utils.check_if_exists(db_notification, modifying=True)

    crud_delete.delete_notifications(db, db_notification)
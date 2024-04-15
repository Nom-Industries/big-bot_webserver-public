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
    prefix="/reminders",
    tags=["Reminders"]
)

@router.get("/", response_model=List[schemas.RemindersBase])
def get_reminders(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_reminders(db, request.query_params._dict))

@router.post("/", response_model=schemas.RemindersBase)
def create_reminders(reminder: schemas.RemindersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_reminders(db, {"reminder_id": reminder.reminder_id}))
    
    return crud_post.insert_reminder(db, reminder)

@router.patch("/", response_model=schemas.RemindersBase)
def update_reminders(reminder: schemas.RemindersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_reminder = crud_get.get_reminders(db, {"reminder_id": reminder.reminder_id})[0]

    utils.check_if_exists(db_reminder, modifying=True)
    
    return crud_patch.update_reminder(db, old_reminder=db_reminder, new_reminder=reminder)

@router.delete("/", status_code=204)
def delete_reminders(reminder: schemas.RemindersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_reminder = crud_get.get_reminders(db, {"reminder_id": reminder.reminder_id})[0]

    utils.check_if_exists(db_reminder, modifying=True)

    crud_delete.delete_reminder(db, db_reminder)
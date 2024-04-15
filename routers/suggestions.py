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
    prefix="/suggestions",
    tags=["Suggestions"]
)

@router.get("/", response_model=List[schemas.SuggestionsMainBase])
def get_suggestions(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_suggestions_channel(db, request.query_params._dict))

@router.post("/", response_model=schemas.SuggestionsMainBase)
def create_suggestions(suggestion: schemas.SuggestionsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_suggestions_channel(db, {"channel_id": suggestion.channel_id}))
    
    return crud_post.insert_suggestion(db, suggestion)

@router.patch("/", response_model=schemas.SuggestionsMainBase)
def update_suggestions(suggestion: schemas.SuggestionsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_suggestion = crud_get.get_suggestions_channel(db, {"channel_id": suggestion.channel_id})[0]

    utils.check_if_exists(db_suggestion, modifying=True)
    
    return crud_patch.update_suggestion(db, old_suggestion=db_suggestion, new_suggestion=suggestion)

@router.delete("/", status_code=204)
def delete_suggestions(suggestion: schemas.SuggestionsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_suggestion = crud_get.get_suggestions_channel(db, {"channel_id": suggestion.channel_id})[0]

    utils.check_if_exists(db_suggestion, modifying=True)

    crud_delete.delete_suggestion_channel(db, db_suggestion)

@router.get("/info", response_model=List[schemas.Suggestions_InfoBase])
def get_suggestion_info(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_suggestions_info(db, request.query_params._dict))

@router.post("/info", response_model=schemas.Suggestions_InfoBase, status_code=201)
def create_suggestion_info(suggestion_info: schemas.Suggestions_InfoBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_suggestions_info(db, {"suggestion_id": suggestion_info.suggestion_id}))

    return crud_post.insert_suggestions_info(db, suggestion_info)

@router.patch("/info", response_model=schemas.Suggestions_InfoBase)
def update_suggestion_info(suggestion_info: schemas.Suggestions_InfoBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_suggestion_info = crud_get.get_suggestions_info(db, {"suggestion_id": suggestion_info.suggestion_id})[0]

    utils.check_if_exists(db_suggestion_info, modifying=True)
    
    return crud_patch.update_suggestions_info(db, old_suggestion_info=db_suggestion_info, new_suggestion_info=suggestion_info)

@router.delete("/info", status_code=204)
def delete_suggestion_info(suggestion_info: schemas.Suggestions_InfoBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_suggestion_info = crud_get.get_suggestions_info(db, {"suggestion_id": suggestion_info.suggestion_id})[0]

    utils.check_if_exists(db_suggestion_info, modifying=True)

    crud_delete.delete_suggestions_info(db, db_suggestion_info)
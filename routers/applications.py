from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

@router.get("/application", response_model=List[schemas.Application_QuestionsBase])
def get_applications(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_applications(db, request.query_params._dict))

@router.post("/application", response_model=schemas.Application_QuestionsBase, status_code=201)
def create_application(application: schemas.Application_QuestionsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_applications(db, {"app_id": application.app_id}))

    return crud_post.insert_application(db, application)

@router.patch("/application", response_model=schemas.Application_QuestionsBase)
def update_application(application: schemas.Application_QuestionsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_application = crud_get.get_applications(db, {"app_id": application.app_id})[0]

    utils.check_if_exists(db_application, modifying=True)
    
    return crud_patch.update_application(db, old_app=db_application, new_app=application)

@router.delete("/application", status_code=204)
def delete_application(application: schemas.Application_QuestionsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_application = crud_get.get_applications(db, {"app_id": application.app_id})[0]

    utils.check_if_exists(db_application, modifying=True)

    crud_delete.delete_application(db, db_application)

@router.get("/responses", response_model=List[schemas.Application_AnswersBase])
def get_application_response(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_application_responses(db, request.query_params._dict))

@router.post("/responses", response_model=schemas.Application_AnswersBase, status_code=201)
def create_application_response(application: schemas.Application_AnswersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_application_responses(db, {"app_id": application.app_id}))

    return crud_post.insert_application_response(db, application)

@router.patch("/responses", response_model=schemas.Application_AnswersBase)
def update_application_response(application: schemas.Application_AnswersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_application = crud_get.get_application_responses(db, {"app_id": application.app_id})

    utils.check_if_exists(db_application, modifying=True)

    return crud_patch.update_application_response(db, old_app=db_application[0], new_app=application)

@router.delete("/responses", status_code=204)
def delete_application_response(application: schemas.Application_AnswersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_application = crud_get.get_application_responses(db, {"app_id": application.app_id})

    utils.check_if_exists(db_application, modifying=True)

    crud_delete.delete_application_response(db, db_application[0])
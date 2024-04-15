from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/reports",
    tags=["Reporting"]
)

@router.get("/", response_model=List[schemas.ReportInfoBase])
def get_reports(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_reports(db, request.query_params._dict))

@router.post("/", response_model=schemas.ReportInfoBase, status_code=201)
def create_report(report: schemas.ReportInfoBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_reports(db, {"message_id": report.message_id}))

    return crud_post.insert_report(db, report)

@router.patch("/", response_model=schemas.ReportInfoBase)
def update_report(report: schemas.ReportInfoBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_report = crud_get.get_reports(db, {"message_id": report.message_id})[0]

    utils.check_if_exists(db_report, modifying=True)
    
    return crud_patch.update_report(db, old_report=db_report, new_report=report)

@router.delete("/", status_code=204)
def delete_report(report: schemas.ReportInfoBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_report = crud_get.get_reports(db, {"message_id": report.message_id})[0]

    utils.check_if_exists(db_report, modifying=True)

    crud_delete.delete_report(db, db_report)

@router.get("/", response_model=List[schemas.ReportMainBase])
def get_report_config(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_report_config(db, request.query_params._dict))

@router.post("/", response_model=schemas.ReportMainBase, status_code=201)
def create_report_config(report_config: schemas.ReportMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_reports(db, {"guild_id": report_config.guild_id}))

    return crud_post.insert_report_config(db, report_config)

@router.patch("/", response_model=schemas.ReportMainBase)
def update_report_config(report_config: schemas.ReportMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_report_config = crud_get.get_report_config(db, {"guild_id": report_config.guild_id})[0]

    utils.check_if_exists(db_report_config, modifying=True)
    
    return crud_patch.update_report_config(db, old_report_config=db_report_config, new_report_config=report_config)

@router.delete("/", status_code=204)
def delete_report_config(report_config: schemas.ReportMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_report_config = crud_get.get_report_config(db, {"guild_id": report_config.guild_id})[0]

    utils.check_if_exists(db_report_config, modifying=True)

    crud_delete.delete_report_config(db, db_report_config)
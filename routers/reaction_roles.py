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
    prefix="/reaction_roles",
    tags=["Reaction Roles"]
)

@router.get("/", response_model=List[schemas.ReactionMainBase])
def get_reaction_role(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_reaction_roles(db, request.query_params._dict))

@router.post("/", response_model=schemas.ReactionMainBase)
def create_reaction_role(reaction_role: schemas.ReactionMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_reaction_roles(db, {"message_id", reaction_role.message_id}))
    
    return crud_post.insert_reaction_role(db, reaction_role)

@router.patch("/", response_model=schemas.ReactionMainBase)
def update_reaction_role(reaction_role: schemas.ReactionMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_reaction_role = crud_get.get_reaction_roles(db, {"message_id", reaction_role.message_id})[0]

    utils.check_if_exists(db_reaction_role, modifying=True)
    
    return crud_patch.update_reaction_role(db, old_reaction_role=db_reaction_role, new_reaction_role=reaction_role)

@router.delete("/", status_code=204)
def delete_reaction_role(reaction_role: schemas.ReactionMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_reaction_role = crud_get.get_reaction_roles(db, {"message_id", reaction_role.message_id})[0]

    utils.check_if_exists(db_reaction_role, modifying=True)

    crud_delete.delete_reaction_roles(db, db_reaction_role)
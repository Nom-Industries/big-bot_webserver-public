import random
from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from fastapi.responses import JSONResponse
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_delete, crud_patch

from typing import List

from string import ascii_letters, digits

import utils

router = APIRouter(
    prefix="/giveaway",
    tags=["Giveaway"]
)

@router.get("/", response_model=List[schemas.GiveawayMainBase])
def get_giveaways(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_giveaways(db, request.query_params._dict))

@router.post("/", response_model=schemas.GiveawayMainBase)
def create_giveaway(giveaway: schemas.GiveawayMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_giveaways(db, {"message_id": giveaway.message_id}))
    
    return crud_post.insert_giveaway(db, giveaway)

@router.patch("/", response_model=schemas.GiveawayMainBase)
def update_giveaway(giveaway: schemas.GiveawayMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway = crud_get.get_giveaways(db, {"message_id": giveaway.message_id})[0]

    utils.check_if_exists(db_giveaway, modifying=True)
    
    return crud_patch.update_giveaway(db, old_giveaway=db_giveaway, new_giveaway=giveaway)

@router.delete("/", status_code=204)
def delete_giveaway(giveaway: schemas.GiveawayMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway = crud_get.get_giveaways(db, {"message_id": giveaway.message_id})[0]

    utils.check_if_exists(db_giveaway, modifying=True)

    crud_delete.delete_giveaway(db, db_giveaway)

@router.get("/blocked", response_model=List[schemas.GiveawayBlockedBase])
def get_giveaway_blocked(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_giveaway_blocked(db, request.query_params._dict))

@router.post("/blocked", response_model=schemas.GiveawayBlockedBase, status_code=201)
def create_giveaway_blocked(giveaway_blocked: schemas.GiveawayBlockedBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_giveaway_blocked(db, {"role_id": giveaway_blocked.role_id}))
    
    return crud_post.insert_giveaway_blocked(db, giveaway_blocked)

@router.patch("/blocked", response_model=schemas.GiveawayBlockedBase)
def update_giveaway_blocked(giveaway_blocked: schemas.GiveawayBlockedBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway_blocked = crud_get.get_giveaway_blocked(db, {"role_id": giveaway_blocked.role_id})[0]

    utils.check_if_exists(db_giveaway_blocked, modifying=True)

    return crud_patch.update_giveaway_blocked(db, old_giveaway_blocked=db_giveaway_blocked, new_giveaway_blocked=giveaway_blocked)

@router.delete("/blocked", response_model=schemas.GiveawayBlockedBase)
def delete_giveaway_blocked(giveaway_blocked: schemas.GiveawayBlockedBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway_blocked = crud_get.get_giveaway_blocked(db, {"role_id": giveaway_blocked.role_id})[0]

    utils.check_if_exists(db_giveaway_blocked, modifying=True)

    crud_delete.delete_giveaway_blocked(db, db_giveaway_blocked)

@router.get("/booster", response_model=List[schemas.GiveawayBoostersBase])
def get_giveaway_booster(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_giveaway_boosters(db, request.query_params._dict))

@router.post("/booster", response_model=schemas.GiveawayBoostersBase, status_code=201)
def create_giveaway_booster(giveaway_booster: schemas.GiveawayBoostersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_giveaway_boosters(db, {"role_id": giveaway_booster.role_id}))
    
    return crud_post.insert_giveaway_booster(db, giveaway_booster)

@router.patch("/booster", response_model=schemas.GiveawayBoostersBase)
def update_giveaway_booster(giveaway_booster: schemas.GiveawayBoostersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway_booster = crud_get.get_giveaway_boosters(db, {"role_id": giveaway_booster.role_id})[0]

    utils.check_if_exists(db_giveaway_booster, modifying=True)

    return crud_patch.update_giveaway_booster(db, old_giveaway_booster=db_giveaway_booster, new_giveaway_booster=giveaway_booster)

@router.delete("/booster", response_model=schemas.GiveawayBoostersBase)
def delete_giveaway_booster(giveaway_booster: schemas.GiveawayBoostersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway_booster = crud_get.get_giveaway_boosters(db, {"role_id": giveaway_booster.role_id})[0]

    utils.check_if_exists(db_giveaway_booster, modifying=True)

    crud_delete.delete_giveaway_booster(db, db_giveaway_booster)

@router.get("/temp_booster", response_model=List[schemas.GiveawayTempBoostersBase])
def get_giveaway_temp_booster(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_giveaway_temp_boosters(db, request.query_params._dict))

@router.post("/temp_booster", response_model=schemas.GiveawayTempBoostersBase)
def create_giveaway_temp_booster(temp_booster: schemas.GiveawayTempBoostersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    invalid = True
    while invalid:    
        try:
            unique_id = ''.join(random.choice(ascii_letters+digits) for i in range(random.randint(6, 10)))
            utils.check_if_exists(crud_get.get_giveaway_temp_boosters(db, {"unique_id": unique_id}))
            invalid = False
        
        except:
            pass

    temp_booster.unique_id = unique_id

    return crud_post.insert_temp_giveaway_booster(db, temp_booster)

@router.patch("/temp_booster", response_model=schemas.GiveawayTempBoostersBase)
def update_giveaway_temp_booster(temp_booster: schemas.GiveawayTempBoostersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway_temp_booster = crud_get.get_giveaway_temp_boosters(db, {"unique_id": temp_booster.unique_id})[0]

    utils.check_if_exists(db_giveaway_temp_booster, modifying=True)
    
    return crud_patch.update_giveaway_temp_boosters(db, old_temp_booster=db_giveaway_temp_booster, new_temp_booster=temp_booster)

@router.delete("/temp_booster", status_code=204)
def delete_giveaway_temp_booster(temp_booster: schemas.GiveawayTempBoostersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_giveaway_temp_booster = crud_get.get_giveaway_temp_boosters(db, {"unique_id": temp_booster.unique_id})[0]

    utils.check_if_exists(db_giveaway_temp_booster, modifying=True)

    crud_delete.delete_giveaway_temp_boosters(db, db_giveaway_temp_booster)
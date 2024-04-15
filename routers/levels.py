from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/levels",
    tags=["Leveling"]
)

@router.get("/config", response_model=List[schemas.Level_MainBase])
def get_level_config(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_level_config(db, request.query_params._dict))

@router.post("/config", response_model=schemas.Level_MainBase, status_code=201)
def create_level_config(level_config: schemas.Level_MainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_level_config(db, {"guild_id": level_config.guild_id}))

    return crud_post.insert_level_config(db, level_config)

@router.patch("/config", response_model=schemas.Level_MainBase)
def update_level_config(level_config: schemas.Level_MainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_level_config = crud_get.get_level_config(db, {"guild_id": level_config.guild_id})[0]

    utils.check_if_exists(db_level_config, modifying=True)
    
    return crud_patch.update_level_config(db, old_level_config=db_level_config, new_level_config=level_config)

@router.delete("/config", status_code=204)
def delete_level_config(level_config: schemas.Level_MainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_level_config = crud_get.get_level_config(db, {"guild_id": level_config.guild_id})[0]

    utils.check_if_exists(db_level_config, modifying=True)

    crud_delete.delete_level_config(db, db_level_config)

@router.get("/roles", response_model=List[schemas.Level_RolesBase])
def get_level_role(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_level_roles(db, request.query_params._dict))

@router.post("/roles", response_model=schemas.Level_RolesBase, status_code=201)
def create_level_role(level_role: schemas.Level_RolesBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_level_roles(db, {"role_id": level_role.role_id}))

    return crud_post.insert_level_roles(db, level_role)

@router.patch("/roles", response_model=schemas.Level_RolesBase)
def update_level_role(level_role: schemas.Level_RolesBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_level_role = crud_get.get_level_roles(db, {"role_id": level_role.role_id})[0]

    utils.check_if_exists(db_level_role, modifying=True)
    
    return crud_patch.update_level_roles(db, old_level_role=db_level_role, new_level_config=level_role)

@router.delete("/roles", status_code=204)
def delete_level_role(level_role: schemas.Level_RolesBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_level_role = crud_get.get_level_roles(db, {"role_id": level_role.role_id})[0]

    utils.check_if_exists(db_level_role, modifying=True)

    crud_delete.delete_level_roles(db, db_level_role)

@router.get("/user", response_model=List[schemas.Level_UsersBase])
def get_level_user(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_level_user(db, request.query_params._dict))

@router.post("/user", response_model=schemas.Level_UsersBase, status_code=201)
def create_level_user(level_user: schemas.Level_UsersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_level_user(db, {"unique_id": level_user.unique_id}))

    return crud_post.insert_level_user(db, level_user)

@router.patch("/user", response_model=schemas.Level_UsersBase)
def update_level_user(level_user: schemas.Level_UsersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_level_user = crud_get.get_level_user(db, {"unique_id": level_user.unique_id})[0]

    utils.check_if_exists(db_level_user, modifying=True)
    
    return crud_patch.update_level_user(db, old_level_user=db_level_user, new_level_user=level_user)

@router.delete("/user", status_code=204)
def delete_level_user(level_user: schemas.Level_UsersBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_level_user = crud_get.get_level_user(db, {"unique_id": level_user.unique_id})[0]

    utils.check_if_exists(db_level_user, modifying=True)

    crud_delete.delete_level_user(db, db_level_user)

@router.get("/aesthetics", response_model=List[schemas.Guild_Level_AestheticsBase])
def get_guild_aesthetics(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_guild_aesthetics(db, request.query_params._dict))

@router.post("/aesthetics", response_model=schemas.Guild_Level_AestheticsBase, status_code=201)
def create_guild_aesthetics(guild: schemas.Guild_Level_AestheticsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_guild_aesthetics(db, {"guild_id": guild.guild_id}))

    return crud_post.insert_guild_aesthetics(db, guild)

@router.patch("/aesthetics", response_model=schemas.Guild_Level_AestheticsBase)
def update_guild_aesthetics(guild: schemas.Guild_Level_AestheticsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_aesthetics(db, {"guild_id": guild.guild_id})[0]

    utils.check_if_exists(db_guild, modifying=True)
    
    return crud_patch.update_guild_aesthetics(db, old_guild=db_guild, new_guild=guild)

@router.delete("/aesthetics", status_code=204)
def delete_guild_aesthetics(guild: schemas.Guild_Level_AestheticsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_aesthetics(db, {"guild_id": guild.guild_id})[0]

    utils.check_if_exists(db_guild, modifying=True)

    crud_delete.delete_guild_aesthetics(db, db_guild)

@router.get("/boosts/roles", response_model=List[schemas.Level_Bonus_RolesBase])
def get_level_boost_roles(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_level_bonus_roles(db, request.query_params._dict))

@router.post("/boosts/roles", response_model=schemas.Level_Bonus_RolesBase, status_code=201)
def create_level_boost_role(role: schemas.Level_Bonus_RolesBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_level_bonus_roles(db, {"role_id": role.role_id}))

    return crud_post.insert_level_boost_role(db, role)

@router.patch("/boosts/roles", response_model=schemas.Level_Bonus_RolesBase)
def update_level_boost_role(role: schemas.Level_Bonus_RolesBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_role = crud_get.get_level_bonus_roles(db, {"role_id": role.role_id})[0]

    utils.check_if_exists(db_role, modifying=True)
    
    return crud_patch.update_level_boost_role(db, old_role=db_role, new_role=role)

@router.delete("/boosts/roles", status_code=204)
def delete_level_boost_role(role: schemas.Level_Bonus_RolesBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_role = crud_get.get_level_bonus_roles(db, {"role_id": role.role_id})[0]

    utils.check_if_exists(db_role, modifying=True)

    crud_delete.delete_level_bonus_role(db, db_role)

@router.get("/boosts/channels", response_model=List[schemas.Level_Bonus_ChannelsBase])
def get_level_boost_channels(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_level_bonus_channels(db, request.query_params._dict))

@router.post("/boosts/channels", response_model=schemas.Level_Bonus_ChannelsBase, status_code=201)
def create_level_boost_channel(channel: schemas.Level_Bonus_ChannelsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_level_bonus_channels(db, {"channel_id": channel.channel_id}))

    return crud_post.insert_level_boost_channel(db, channel)

@router.patch("/boosts/channels", response_model=schemas.Level_Bonus_ChannelsBase)
def update_level_boost_channel(channel: schemas.Level_Bonus_ChannelsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_channel = crud_get.get_level_bonus_channels(db, {"channel_id": channel.channel_id})[0]

    utils.check_if_exists(db_channel, modifying=True)
    
    return crud_patch.update_level_boost_channel(db, old_channel=db_channel, new_channel=channel)

@router.delete("/boosts/channels", status_code=204)
def delete_level_boost_channel(channel: schemas.Level_Bonus_ChannelsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_channel = crud_get.get_level_bonus_channels(db, {"channel_id": channel.channel_id})[0]

    utils.check_if_exists(db_channel, modifying=True)

    crud_delete.delete_level_bonus_channel(db, db_channel)
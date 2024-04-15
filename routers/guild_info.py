from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from fastapi.responses import JSONResponse
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_delete, crud_patch

from typing import List

import utils

guild_main_router = APIRouter(
    prefix="/guild/main",
    tags=["Guild Info"]
)

guild_stats_router = APIRouter(
    prefix="/guild/stats",
    tags=["Guild Stats Channels"]
)

guild_mod_router = APIRouter(
    prefix="/guild/mod",
    tags=["Guild Mod"]
)

guild_logging_config_router = APIRouter(
    prefix="/guild/logging",
    tags=["Guild Logging"]
)

@guild_main_router.get("/", response_model=List[schemas.GuildMainBase])
def get_guild_data(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_guild_info(db, request.query_params._dict))

@guild_main_router.post("/", response_model=schemas.GuildMainBase, status_code=201)
def create_guild_data(guild: schemas.GuildMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_guild_info(db, {"guild_id": guild.guild_id}))

    return crud_post.insert_guild_info(db, guild)

@guild_main_router.patch("/", response_model=schemas.GuildMainBase)
def update_guild_data(guild: schemas.GuildMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_info(db, {"guild_id": guild.guild_id})[0]

    utils.check_if_exists(db_guild, modifying=True)
    
    return crud_patch.update_guild_info(db, old_guild=db_guild, new_guild=guild)

@guild_main_router.delete("/", status_code=204)
def delete_guild_data(guild: schemas.GuildMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_info(db, {"guild_id": guild.guild_id})[0]

    utils.check_if_exists(db_guild, modifying=True)

    crud_delete.delete_guild_info(db, db_guild)

@guild_stats_router.get("/", response_model=List[schemas.ServerstatsMainBase])
def get_guild_stats_channel(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_guild_stats(db, request.query_params._dict))

@guild_stats_router.post("/", response_model=schemas.ServerstatsMainBase, status_code=201)
def create_guild_stats(guild: schemas.ServerstatsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_guild_stats(db, {"channel_id": guild.channel_id}))
    
    return crud_post.insert_guild_stats(db, guild)

@guild_stats_router.patch("/", response_model=schemas.ServerstatsMainBase)
def update_guild_stats(guild: schemas.ServerstatsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_stats(db, {"channel_id": guild.channel_id})[0]

    utils.check_if_exists(db_guild, modifying=True)

    return crud_patch.update_guild_stats(db, old_guild=db_guild, new_guild=guild)

@guild_stats_router.delete("/", response_model=schemas.ServerstatsMainBase)
def delete_guild_stats(guild: schemas.ServerstatsMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_stats(db, {"channel_id": guild.channel_id})[0]

    utils.check_if_exists(db_guild, modifying=True)

    crud_delete.delete_guild_stats(db, db_guild)

@guild_mod_router.get("/logs", response_model=List[schemas.GuildModBase])
def get_guild_mod_logs(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_guild_mod_data(db, request.query_params._dict))

@guild_mod_router.post("/logs", response_model=schemas.GuildModBase, status_code=201)
def create_guild_mod_log(mod_log: schemas.GuildModBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_guild_mod_data(db, {"punishment_id": mod_log.punishment_id}))

    return crud_post.insert_guild_mod_log(db, mod_log)

@guild_mod_router.patch("/logs", response_model=schemas.GuildModBase)
def update_guild_mod_log(mod_log: schemas.GuildModBaseModify, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_mod_log = crud_get.get_guild_mod_data(db, {"punishment_id": mod_log.punishment_id})[0]

    utils.check_if_exists(db_mod_log, modifying=True)
    
    return crud_patch.update_guild_modlog(db, old_mod_log=db_mod_log, new_mod_log=mod_log)

@guild_mod_router.delete("/logs", status_code=204)
def delete_guild_mod_log(mod_log: schemas.GuildModBaseModify, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_mod_log = crud_get.get_guild_mod_data(db, {"punishment_id": mod_log.punishment_id})[0]

    utils.check_if_exists(db_mod_log, modifying=True)

    crud_delete.delete_guild_modlog(db, db_mod_log)

@guild_mod_router.get("/main", response_model=List[schemas.ModerationMainBase])
def get_mod_main(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_mod_main(db, request.query_params._dict))

@guild_mod_router.post("/main", response_model=schemas.ModerationMainBase, status_code=201)
def create_mod_main(mod: schemas.ModerationMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_mod_main(db, {"guild": mod.guild}))

    return crud_post.insert_mod_main(db, mod)

@guild_mod_router.patch("/main", response_model=schemas.ModerationMainBase)
def update_mod_main(mod: schemas.ModerationMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_mod = crud_get.get_mod_main(db, {"guild": mod.guild})[0]

    utils.check_if_exists(db_mod, modifying=True)
    
    return crud_patch.update_mod_main(db, old_mod=db_mod, new_mod=mod)

@guild_mod_router.delete("/main", status_code=204)
def delete_mod_main(mod: schemas.ModerationMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_mod = crud_get.get_mod_main(db, {"guild": mod.guild})[0]

    utils.check_if_exists(db_mod, modifying=True)

    crud_delete.delete_mod_main(db, db_mod)

@guild_logging_config_router.get("/", response_model=List[schemas.LoggingMainBase])
def get_guild_logging_configuration(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_guild_logging_config(db, request.query_params._dict))

@guild_logging_config_router.post("/", response_model=schemas.LoggingMainBase, status_code=201)
def create_guild_logging_config(guild: schemas.LoggingMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_guild_logging_config(db, {"webhook_link": guild.webhook_link}))

    return crud_post.insert_guild_logging_config(db, guild)

@guild_logging_config_router.patch("/", response_model=schemas.LoggingMainBase)
def update_guild_logging_config(guild: schemas.LoggingMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_logging_config(db, {"webhook_link": guild.webhook_link})[0]

    utils.check_if_exists(db_guild, modifying=True)
    
    return crud_patch.update_guild_log_config(db, old_guild=db_guild, new_guild=guild)

@guild_logging_config_router.delete("/", status_code=204)
def delete_guild_logging_config(guild: schemas.LoggingMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_guild = crud_get.get_guild_logging_config(db, {"webhook_link": guild.webhook_link})[0]

    utils.check_if_exists(db_guild, modifying=True)

    crud_delete.delete_guild_log_config(db, db_guild)
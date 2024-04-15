from fastapi import APIRouter, Depends, Request
from fastapi.security.api_key import APIKey
from designs import schemas
from sqlalchemy.orm import Session
from database.database import get_db
from crud import crud_get, crud_post, crud_patch, crud_delete

from typing import List

import utils

router = APIRouter(
    prefix="/support",
    tags=["Support"]
)

@router.get("/tickets", response_model=List[schemas.CurrentTicketsBase])
def get_open_tickets(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_current_tickets(db, request.query_params._dict))

@router.post("/tickets", response_model=schemas.CurrentTicketsBase, status_code=201)
def create_ticket(ticket: schemas.CurrentTicketsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_current_tickets(db, {"channel_id": ticket.channel_id}))

    return crud_post.insert_ticket(db, ticket)

@router.patch("/tickets", response_model=schemas.CurrentTicketsBase)
def update_ticket(ticket: schemas.CurrentTicketsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_ticket = crud_get.get_current_tickets(db, {"channel_id": ticket.channel_id})[0]

    utils.check_if_exists(db_ticket, modifying=True)
    
    return crud_patch.update_ticket_detail(db, old_ticket=db_ticket, new_ticket=ticket)

@router.delete("/tickets", status_code=204)
def delete_ticket(ticket: schemas.CurrentTicketsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_ticket = crud_get.get_current_tickets(db, {"channel_id": ticket.channel_id})[0]

    utils.check_if_exists(db_ticket, modifying=True)

    crud_delete.delete_ticket_detail(db, db_ticket)

@router.get("/config", response_model=List[schemas.SupportMainBase])
def get_support_config(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_support_data(db, request.query_params._dict))

@router.post("/config", response_model=schemas.SupportMainBase, status_code=201)
def create_support_config(ticket_config: schemas.SupportMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_support_data(db, {"message_id": ticket_config.message_id}))

    return crud_post.insert_ticket(db, ticket_config)

@router.patch("/config", response_model=schemas.SupportMainBase)
def update_support_config(ticket_config: schemas.SupportMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_ticket_config = crud_get.get_support_data(db, {"message_id": ticket_config.message_id})[0]

    utils.check_if_exists(db_ticket_config, modifying=True)
    
    return crud_patch.update_ticket_config_detail(db, old_ticket_config=db_ticket_config, new_ticket_config=ticket_config)

@router.delete("/config", status_code=204)
def delete_support_config(ticket_config: schemas.SupportMainBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_ticket_config = crud_get.get_support_data(db, {"message_id": ticket_config.message_id})[0]

    utils.check_if_exists(db_ticket_config, modifying=True)

    crud_delete.delete_ticket_config_detail(db, db_ticket_config)

@router.get("/blacklists", response_model=List[schemas.TicketBlacklistsBase])
def get_ticket_blacklists(request: Request, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    request.query_params._dict.pop("api_key")

    return utils.return_response(crud_get.get_ticket_blacklists(db, request.query_params._dict))

@router.post("/blacklists", response_model=schemas.TicketBlacklistsBase, status_code=201)
def create_ticket_blacklist(blacklisted: schemas.TicketBlacklistsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    utils.check_if_exists(crud_get.get_ticket_blacklists(db, {"member": blacklisted.member, "guild": blacklisted.guild}))

    return crud_post.insert_ticket_blacklist(db, blacklisted)

@router.patch("/blacklists", response_model=schemas.TicketBlacklistsBase)
def update_ticket_blacklists(blacklisted: schemas.TicketBlacklistsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_ticket_blacklist = crud_get.get_ticket_blacklists(db, {"member": blacklisted.member, "guild": blacklisted.guild})[0]

    utils.check_if_exists(db_ticket_blacklist, modifying=True)

    return crud_patch.update_ticket_blacklist(db, old_blacklist=db_ticket_blacklist, new_blacklist=blacklisted)

@router.delete("/blacklists", response_model=schemas.TicketBlacklistsBase)
def delete_ticket_blacklist(blacklisted: schemas.TicketBlacklistsBase, api_key: APIKey = Depends(utils.validate_api_key), db: Session = Depends(get_db)):
    db_ticket_blacklist = crud_get.get_ticket_blacklists(db, {"member": blacklisted.member, "guild": blacklisted.guild})[0]

    utils.check_if_exists(db_ticket_blacklist, modifying=True)

    crud_delete.delete_ticket_blacklist(db, db_ticket_blacklist)
import json
from typing import List
from sqlalchemy.orm import Session

from designs import models, schemas

from fastapi import HTTPException, status

def update_guild_info(db: Session, old_guild: schemas.GuildMainBase, new_guild: schemas.GuildMainBase):
    if old_guild == new_guild:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_guild.dict():
        if not new_guild.__fields__[i]:
            new_guild.__fields__[i] = old_guild.__fields__[i]

    db_guild = db.query(models.GuildMain).filter(models.GuildMain.guild_id == old_guild.guild_id)
    db_guild.update({**new_guild.dict()})
    db.commit()
    return db.query(models.GuildMain).filter(models.GuildMain.guild_id == old_guild.guild_id).first()

def update_guild_stats(db: Session, old_guild: schemas.ServerstatsMainBase, new_guild: schemas.ServerstatsMainBase):
    if old_guild == new_guild:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_guild.dict():
        if not new_guild.__fields__[i]:
            new_guild.__fields__[i] = old_guild.__fields__[i]
    
    db_guild = db.query(models.ServerstatsMain).filter(models.ServerstatsMain.channel_id == old_guild.channel_id)
    db_guild.update({**new_guild.dict()})
    db.commit()
    return db.query(models.ServerstatsMain).filter(models.ServerstatsMain.channel_id == old_guild.channel_id).first()

def update_mod_main(db: Session, old_mod: schemas.ModerationMainBase, new_mod: schemas.ModerationMainBase):
    if old_mod == new_mod:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_mod.dict():
        if not new_mod.__fields__[i]:
            new_mod.__fields__[i] = old_mod.__fields__[i]
    
    db_mod = db.query(models.ModerationMain).filter(models.ModerationMain.guild == old_mod.guild)
    db_mod.update({**new_mod.dict()})
    db.commit()
    return db.query(models.ModerationMain).filter(models.ModerationMain.guild == old_mod.guild).first()

def update_guild_modlog(db: Session, old_mod_log: schemas.GuildModBase, new_mod_log: schemas.GuildModBase):
    if old_mod_log == new_mod_log:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_mod_log.dict():
        if not new_mod_log.__fields__[i]:
            new_mod_log.__fields__[i] = old_mod_log.__fields__[i]

    db_mod_log = db.query(models.GuildMod).filter(models.GuildMod.punishment_id == old_mod_log.punishment_id)
    db_mod_log.update({**new_mod_log.dict()})
    db.commit()
    return db.query(models.GuildMod).filter(models.GuildMod.punishment_id == old_mod_log.punishment_id).first()

def update_guild_log_config(db: Session, old_guild: schemas.LoggingMainBase, new_guild: schemas.LoggingMainBase):
    if old_guild == new_guild:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_guild.dict():
        if not new_guild.__fields__[i]:
            new_guild.__fields__[i] = old_guild.__fields__[i]
    
    if "channel_channel_blacklist" in new_guild.__dict__:
        new_guild.__dict__["channel_channel_blacklist"] = str(new_guild.__dict__["channel_channel_blacklist"])

    if "role_role_blacklist" in new_guild.__dict__:
        new_guild.__dict__["role_role_blacklist"] = str(new_guild.__dict__["role_role_blacklist"])

    db_guild = db.query(models.LoggingMain).filter(models.LoggingMain.webhook_link == old_guild.webhook_link)
    db_guild.update({**new_guild.dict()})
    db.commit()

    db_guild.channel_channel_blacklist = json.loads(db_guild.channel_channel_blacklist)
    db_guild.role_role_blacklist = json.loads(db_guild.role_role_blacklist)

    return db.query(models.LoggingMain).filter(models.LoggingMain.webhook_link == old_guild.webhook_link).first()

def update_auto_thread_detail(db: Session, old_auto_thread: schemas.AutoThreadMainBase, new_auto_thread: schemas.AutoThreadMainBase):
    if old_auto_thread == new_auto_thread:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_auto_thread.dict():
        if not new_auto_thread.__fields__[i]:
            new_auto_thread.__fields__[i] = old_auto_thread.__fields__[i]

    db_auto_thread = db.query(models.AutoThreadMain).filter(models.AutoThreadMain.channel_id == old_auto_thread.channel_id)
    db_auto_thread.update({**new_auto_thread.dict()})
    db.commit()
    return db.query(models.AutoThreadMain).filter(models.AutoThreadMain.channel_id == old_auto_thread.channel_id).first()

def update_economy_player_detail(db: Session, old_user: schemas.EconomyMainBase, new_user: schemas.EconomyMainBase):
    if old_user == new_user:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_user.dict():
        if not new_user.__fields__[i]:
            new_user.__fields__[i] = old_user.__fields__[i]

    db_economy_player = db.query(models.EconomyMain).filter(models.EconomyMain.user_id == old_user.user_id)
    db_economy_player.update({**new_user.dict()})
    db.commit()
    return db.query(models.EconomyMain).filter(models.EconomyMain.user_id == old_user.user_id).first()

def update_private_voice_channel_detail(db: Session, old_channel: schemas.VoiceChannelsBase, new_channel: schemas.VoiceChannelsBase):
    if old_channel == new_channel:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_channel.dict():
        if not new_channel.__fields__[i]:
            new_channel.__fields__[i] = old_channel.__fields__[i]

    db_channel = db.query(models.VoiceChannels).filter(models.VoiceChannels.owner_id == old_channel.owner_id)
    db_channel.update({**new_channel.dict()})
    db.commit()
    return db.query(models.VoiceChannels).filter(models.VoiceChannels.owner_id == new_channel.owner_id).first()

def update_private_voice_channel_config_detail(db: Session, old_channel: schemas.VoiceChannelsMainBase, new_channel: schemas.VoiceChannelsMainBase):
    if old_channel == new_channel:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_channel.dict():
        if not new_channel.__fields__[i]:
            new_channel.__fields__[i] = old_channel.__fields__[i]

    db_channel = db.query(models.VoiceChannelsMain).filter(models.VoiceChannelsMain.channel_id == old_channel.channel_id)
    db_channel.update({**new_channel.dict()})
    db.commit()
    return db.query(models.VoiceChannelsMain).filter(models.VoiceChannelsMain.channel_id == new_channel.channel_id).first()

def update_sticky_message_detail(db: Session, old_sticky_message: schemas.StickyMainBase, new_sticky_message: schemas.StickyMainBase):
    if old_sticky_message == new_sticky_message:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_sticky_message.dict():
        if not new_sticky_message.__fields__[i]:
            new_sticky_message.__fields__[i] = old_sticky_message.__fields__[i]

    db_channel = db.query(models.StickyMain).filter(models.StickyMain.channel_id == old_sticky_message.channel_id)
    db_channel.update({**new_sticky_message.dict()})
    db.commit()
    return db.query(models.StickyMain).filter(models.StickyMain.channel_id == new_sticky_message.channel_id).first()

def update_ticket_detail(db: Session, old_ticket: schemas.CurrentTicketsBase, new_ticket: schemas.CurrentTicketsBase):
    if old_ticket == new_ticket:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_ticket.dict():
        if not new_ticket.__fields__[i]:
            new_ticket.__fields__[i] = old_ticket.__fields__[i]

    db_channel = db.query(models.CurrentTickets).filter(models.CurrentTickets.author_id == old_ticket.author_id)
    db_channel.update({**new_ticket.dict()})
    db.commit()
    return db.query(models.CurrentTickets).filter(models.CurrentTickets.author_id == new_ticket.author_id).first()

def update_ticket_config_detail(db: Session, old_ticket_config: schemas.SupportMainBase, new_ticket_config: schemas.SupportMainBase):
    if old_ticket_config == new_ticket_config:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_ticket_config.dict():
        if not new_ticket_config.__fields__[i]:
            new_ticket_config.__fields__[i] = old_ticket_config.__fields__[i]

    db_channel = db.query(models.SupportMain).filter(models.SupportMain.message_id == old_ticket_config.message_id)
    db_channel.update({**new_ticket_config.dict()})
    db.commit()
    return db.query(models.SupportMain).filter(models.SupportMain.message_id == new_ticket_config.message_id).first()

def update_ticket_blacklist(db: Session, old_blacklist: schemas.SupportMainBase, new_blacklist: schemas.SupportMainBase):
    if old_blacklist == new_blacklist:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_blacklist.dict():
        if not new_blacklist.__fields__[i]:
            new_blacklist.__fields__[i] = old_blacklist.__fields__[i]

    db_blacklist = db.query(models.SupportMain).filter(models.SupportMain.message_id == old_blacklist.message_id)
    db_blacklist.update({**new_blacklist.dict()})
    db.commit()
    return db.query(models.SupportMain).filter(models.SupportMain.message_id == old_blacklist.message_id).first()

def update_giveaway(db: Session, old_giveaway: schemas.GiveawayMainBase, new_giveaway: schemas.GiveawayMainBase):
    if old_giveaway == new_giveaway:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_giveaway.dict():
        if not new_giveaway.__fields__[i]:
            new_giveaway.__fields__[i] = old_giveaway.__fields__[i]

    new_giveaway.__dict__["entrants"] = str(new_giveaway.__dict__["entrants"])
    new_giveaway.__dict__["allowedroles"] = str(new_giveaway.__dict__["allowedroles"])
    new_giveaway.__dict__["blockedroles"] = str(new_giveaway.__dict__["blockedroles"])
    new_giveaway.__dict__["bypassroles"] = str(new_giveaway.__dict__["bypassroles"])

    db_giveaway = db.query(models.GiveawayMain).filter(models.GiveawayMain.message_id == old_giveaway.message_id)
    db_giveaway.update({**new_giveaway.dict()})
    db.commit()

    db_response = db.query(models.GiveawayMain).filter(models.GiveawayMain.message_id == old_giveaway.message_id).first()
    db_response.entrants = json.loads(db_response.entrants)
    db_response.allowedroles = json.loads(db_response.allowedroles)
    db_response.blockedroles = json.loads(db_response.blockedroles)
    db_response.bypassroles = json.loads(db_response.bypassroles)

    return db.query(models.GiveawayMain).filter(models.GiveawayMain.message_id == old_giveaway.message_id).first()

def update_giveaway_blocked(db: Session, old_giveaway_blocked: schemas.GiveawayBlockedBase, new_giveaway_blocked: schemas.GiveawayBlockedBase):
    if old_giveaway_blocked == new_giveaway_blocked:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_giveaway_blocked.dict():
        if not new_giveaway_blocked.__fields__[i]:
            new_giveaway_blocked.__fields__[i] = old_giveaway_blocked.__fields__[i]

    db_giveaway_blocked = db.query(models.GiveawayBlocked).filter(models.GiveawayBlocked.role_id == new_giveaway_blocked.role_id)
    db_giveaway_blocked.update({**new_giveaway_blocked.dict()})
    db.commit()
    return db.query(models.GiveawayBlocked).filter(models.GiveawayBlocked.role_id == new_giveaway_blocked.role_id).first()

def update_giveaway_booster(db: Session, old_giveaway_booster: schemas.GiveawayBlockedBase, new_giveaway_booster: schemas.GiveawayBlockedBase):
    if old_giveaway_booster == new_giveaway_booster:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_giveaway_booster.dict():
        if not new_giveaway_booster.__fields__[i]:
            new_giveaway_booster.__fields__[i] = old_giveaway_booster.__fields__[i]

    db_giveaway_blocked = db.query(models.GiveawayBoosters).filter(models.GiveawayBoosters.role_id == new_giveaway_booster.role_id)
    db_giveaway_blocked.update({**new_giveaway_booster.dict()})
    db.commit()
    return db.query(models.GiveawayBoosters).filter(models.GiveawayBoosters.role_id == new_giveaway_booster.role_id).first()

def update_suggestion(db: Session, old_suggestion: schemas.SuggestionsMainBase, new_suggestion: schemas.SuggestionsMainBase):
    if old_suggestion == new_suggestion:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_suggestion.dict():
        if not new_suggestion.__fields__[i]:
            new_suggestion.__fields__[i] = old_suggestion.__fields__[i]

    db_suggestion = db.query(models.SuggestionsMain).filter(models.SuggestionsMain.channel_id == new_suggestion.channel_id)
    db_suggestion.update({**new_suggestion.dict()})
    db.commit()
    return db.query(models.SuggestionsMain).filter(models.SuggestionsMain.channel_id == new_suggestion.channel_id).first()

def update_nickname_config(db: Session, old_nickname: schemas.NicknameMainBase, new_nickname: schemas.NicknameMainBase):
    if old_nickname == new_nickname:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_nickname.dict():
        if not new_nickname.__fields__[i]:
            new_nickname.__fields__[i] = old_nickname.__fields__[i]

    db_nickname = db.query(models.NicknameMain).filter(models.NicknameMain.guild_id == new_nickname.guild_id)
    db_nickname.update({**new_nickname.dict()})
    db.commit()
    return db.query(models.NicknameMain).filter(models.NicknameMain.guild_id == new_nickname.guild_id).first()

def update_nickname_request(db: Session, old_nickname_request: schemas.NicknameRequestsBase, new_nickname_request: schemas.NicknameRequestsBase):
    if old_nickname_request == new_nickname_request:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_nickname_request.dict():
        if not new_nickname_request.__fields__[i]:
            new_nickname_request.__fields__[i] = old_nickname_request.__fields__[i]

    db_nickname_request = db.query(models.NicknameRequests).filter(models.NicknameRequests.message_id == new_nickname_request.message_id)
    db_nickname_request.update({**new_nickname_request.dict()})
    db.commit()
    return db.query(models.NicknameRequests).filter(models.NicknameRequests.message_id == new_nickname_request.message_id).first()

def update_reaction_role(db: Session, old_reaction_role: schemas.ReactionMainBase, new_reaction_role: schemas.ReactionMainBase):
    if old_reaction_role == new_reaction_role:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_reaction_role.dict():
        if not new_reaction_role.__fields__[i]:
            new_reaction_role.__fields__[i] = old_reaction_role.__fields__[i]

    db_reaction_role = db.query(models.ReactionMain).filter(models.ReactionMain.message_id == new_reaction_role.message_id)
    db_reaction_role.update({**new_reaction_role.dict()})
    db.commit()
    return db.query(models.ReactionMain).filter(models.ReactionMain.message_id == new_reaction_role.message_id).first()

def update_autopublish_channels(db: Session, old_autopublish: schemas.AutopublishBase, new_autopublish: schemas.AutopublishBase):
    if old_autopublish == new_autopublish:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_autopublish.dict():
        if not new_autopublish.__fields__[i]:
            new_autopublish.__fields__[i] = old_autopublish.__fields__[i]

    db_autopublish = db.query(models.Autopublish).filter(models.Autopublish.channel_id == new_autopublish.channel_id)
    db_autopublish.update({**new_autopublish.dict()})
    db.commit()
    return db.query(models.Autopublish).filter(models.Autopublish.channel_id == new_autopublish.channel_id).first()

def update_economy_user_settings(db: Session, old_economy_user: schemas.Economy_User_SettingsBase, new_economy_user: schemas.Economy_User_SettingsBase):
    if old_economy_user == new_economy_user:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_economy_user.dict():
        if not new_economy_user.__fields__[i]:
            new_economy_user.__fields__[i] = old_economy_user.__fields__[i]

    db_economy_user = db.query(models.Economy_User_Settings).filter(models.Economy_User_Settings.user == new_economy_user.user)
    db_economy_user.update({**new_economy_user.dict()})
    db.commit()
    return db.query(models.Economy_User_Settings).filter(models.Economy_User_Settings.user == new_economy_user.user).first()

def update_level_config(db: Session, old_level_config: schemas.Level_MainBase, new_level_config: schemas.Level_MainBase):
    if old_level_config == new_level_config:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_level_config.dict():
        if not new_level_config.__fields__[i]:
            new_level_config.__fields__[i] = old_level_config.__fields__[i]

    db_level_config = db.query(models.Level_Main).filter(models.Level_Main.guild_id == new_level_config.guild_id)
    db_level_config.update({**new_level_config.dict()})
    db.commit()
    return db.query(models.Level_Main).filter(models.Level_Main.guild_id == new_level_config.guild_id).first()

def update_level_roles(db: Session, old_level_role: schemas.Level_RolesBase, new_level_role: schemas.Level_RolesBase):
    if old_level_role == new_level_role:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_level_role.dict():
        if not new_level_role.__fields__[i]:
            new_level_role.__fields__[i] = old_level_role.__fields__[i]

    db_level_roles = db.query(models.Level_Roles).filter(models.Level_Roles.role_id == new_level_role.role_id)
    db_level_roles.update({**new_level_role.dict()})
    db.commit()
    return db.query(models.Level_Roles).filter(models.Level_Roles.role_id == new_level_role.role_id).first()

def update_level_user(db: Session, old_level_user: schemas.Level_UsersBase, new_level_user: schemas.Level_UsersBase):
    if old_level_user == new_level_user:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_level_user.dict():
        if not new_level_user.__fields__[i]:
            new_level_user.__fields__[i] = old_level_user.__fields__[i]

    db_level_user = db.query(models.Level_Users).filter(models.Level_Users.unique_id == new_level_user.unique_id)
    db_level_user.update({**new_level_user.dict()})
    db.commit()
    return db.query(models.Level_Users).filter(models.Level_Users.unique_id == new_level_user.unique_id).first()

def update_notifications(db: Session, old_notifications: schemas.NotificationsBase, new_notifications: schemas.NotificationsBase):
    if old_notifications == new_notifications:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_notifications.dict():
        if not new_notifications.__fields__[i]:
            new_notifications.__fields__[i] = old_notifications.__fields__[i]

    db_notifications = db.query(models.Notifications).filter(models.Notifications.channel_id == new_notifications.channel_id)
    db_notifications.update({**new_notifications.dict()})
    db.commit()
    return db.query(models.Notifications).filter(models.Notifications.channel_id == new_notifications.channel_id).first()

def update_suggestions_info(db: Session, old_suggestion_info: schemas.Suggestions_InfoBase, new_suggestion_info: schemas.Suggestions_InfoBase):
    if old_suggestion_info == new_suggestion_info:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_suggestion_info.dict():
        if not new_suggestion_info.__fields__[i]:
            new_suggestion_info.__fields__[i] = old_suggestion_info.__fields__[i]

    new_suggestion_info.__dict__["upvotes"] = str(new_suggestion_info.__dict__["upvotes"])
    new_suggestion_info.__dict__["downvotes"] = str(new_suggestion_info.__dict__["downvotes"])

    db_suggestion_info = db.query(models.Suggestions_Info).filter(models.Suggestions_Info.suggestion_id == new_suggestion_info.suggestion_id)
    db_suggestion_info.update({**new_suggestion_info.dict()})
    db.commit()

    db_response = db.query(models.Suggestions_Info).filter(models.Suggestions_Info.suggestion_id == new_suggestion_info.suggestion_id).first()
    db_response.upvotes = json.loads(db_response.upvotes)
    db_response.downvotes = json.loads(db_response.downvotes)

    return db_response

def update_guild_aesthetics(db: Session, old_guild: schemas.Guild_Level_AestheticsBase, new_guild: schemas.Guild_Level_AestheticsBase):
    if old_guild == new_guild:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_guild.dict():
        if not new_guild.__fields__[i]:
            new_guild.__fields__[i] = old_guild.__fields__[i]

    db_guild = db.query(models.Guild_Level_Aesthetics).filter(models.Guild_Level_Aesthetics.guild_id == new_guild.guild_id)
    db_guild.update({**new_guild.dict()})
    db.commit()
    return db.query(models.Guild_Level_Aesthetics).filter(models.Guild_Level_Aesthetics.guild_id == new_guild.guild_id).first()

def update_application(db: Session, old_app: schemas.Application_QuestionsBase, new_app: schemas.Application_QuestionsBase):
    if old_app == new_app:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_app.dict():
        if not new_app.__fields__[i]:
            new_app.__fields__[i] = old_app.__fields__[i]
    
    if "questions" in new_app.__dict__:
        new_app.__dict__["questions"] = "[" + ', '.join(f'&#39;{i}&#39;' for i in new_app.__dict__["questions"]) + "]"
    
    if "roles_required" in new_app.__dict__:
        new_app.__dict__["roles_required"] = str([i for i in new_app.__dict__["roles_required"]]).replace("'", '"')

    db_app = db.query(models.Application_Questions).filter(models.Application_Questions.app_id == new_app.app_id)
    db_app.update({**new_app.dict()})
    db.commit()
    
    db_response = db.query(models.Application_Questions).filter(models.Application_Questions.app_id == new_app.app_id).first()
    db_response.questions = json.loads(db_response.questions.replace("&#39;", '"'))
    db_response.roles_required = json.loads(db_response.roles_required)

    return db_response

def update_application_response(db: Session, old_app: schemas.Application_AnswersBase, new_app: schemas.Application_AnswersBase):
    if old_app == new_app:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_app.dict():
        if not new_app.__fields__[i]:
            new_app.__fields__[i] = old_app.__fields__[i]

    if "q_a" in new_app.__dict__:
        new_app.__dict__["q_a"] = "{" + ', '.join(f'&#39;{j}&#39;: &#39;{new_app.__dict__["q_a"][j]}&#39;' for j in new_app.__dict__["q_a"]) + "}"

    db_app = db.query(models.Application_Answers).filter(models.Application_Answers.app_id == new_app.app_id)
    db_app.update({**new_app.dict()})
    db.commit()
    
    db_response = db.query(models.Application_Answers).filter(models.Application_Answers.app_id == new_app.app_id).first()
    db_response.q_a = json.loads(db_response.q_a.replace("&#39;", '"'))
    
    return db_response

def update_level_boost_role(db: Session, old_role: schemas.Level_Bonus_RolesBase, new_role: schemas.Level_Bonus_RolesBase):
    if old_role == new_role:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_role.dict():
        if not new_role.__fields__[i]:
            new_role.__fields__[i] = old_role.__fields__[i]

    db_role = db.query(models.Level_Bonus_Roles).filter(models.Level_Bonus_Roles.role_id == new_role.role_id)
    db_role.update({**new_role.dict()})
    db.commit()
    return db.query(models.Level_Bonus_Roles).filter(models.Level_Bonus_Roles.role_id == new_role.role_id).first()

def update_level_boost_channel(db: Session, old_channel: schemas.Level_Bonus_ChannelsBase, new_channel: schemas.Level_Bonus_ChannelsBase):
    if old_channel == new_channel:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_channel.dict():
        if not new_channel.__fields__[i]:
            new_channel.__fields__[i] = old_channel.__fields__[i]

    db_channel = db.query(models.Level_Bonus_Channels).filter(models.Level_Bonus_Channels.channel_id == new_channel.channel_id)
    db_channel.update({**new_channel.dict()})
    db.commit()
    return db.query(models.Level_Bonus_Channels).filter(models.Level_Bonus_Channels.channel_id == new_channel.channel_id).first()

def update_reminder(db: Session, old_reminder: schemas.RemindersBase, new_reminder: schemas.RemindersBase):
    if old_reminder == new_reminder:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_reminder.dict():
        if not new_reminder.__fields__[i]:
            new_reminder.__fields__[i] = old_reminder.__fields__[i]

    db_reminder = db.query(models.Reminders).filter(models.Reminders.reminder_id == new_reminder.reminder_id)
    db_reminder.update({**new_reminder.dict()})
    db.commit()
    return db.query(models.Reminders).filter(models.Reminders.reminder_id == new_reminder.reminder_id).first()

def update_user_statistics(db: Session, old_user_stats: schemas.UserStatisticsBase, new_user_stats: schemas.UserStatisticsBase):
    if old_user_stats == new_user_stats:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_user_stats.dict():
        if not new_user_stats.__fields__[i]:
            new_user_stats.__fields__[i] = old_user_stats.__fields__[i]

    db_user_statistics = db.query(models.UserStatistics).filter(models.UserStatistics.unique_id == new_user_stats.unique_id)
    db_user_statistics.update({**new_user_stats.dict()})
    db.commit()
    return db.query(models.UserStatistics).filter(models.UserStatistics.unique_id == new_user_stats.unique_id).first()

def update_giveaway_temp_boosters(db: Session, old_temp_booster: schemas.GiveawayTempBoostersBase, new_temp_booster: schemas.GiveawayTempBoostersBase):
    if old_temp_booster == new_temp_booster:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_temp_booster.dict():
        if not new_temp_booster.__fields__[i]:
            new_temp_booster.__fields__[i] = old_temp_booster.__fields__[i]

    db_temp_booster = db.query(models.GiveawayTempBoosters).filter(models.GiveawayTempBoosters.unique_id == new_temp_booster.unique_id)
    db_temp_booster.update({**new_temp_booster.dict()})
    db.commit()
    return db.query(models.GiveawayTempBoosters).filter(models.GiveawayTempBoosters.unique_id == new_temp_booster.unique_id).first()

def update_report(db: Session, old_report: schemas.ReportInfoBase, new_report: schemas.ReportInfoBase):
    if old_report == new_report:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_report.dict():
        if not new_report.__fields__[i]:
            new_report.__fields__[i] = old_report.__fields__[i]

    db_report = db.query(models.ReportInfo).filter(models.ReportInfo.message_id == new_report.message_id)
    db_report.update({**new_report.dict()})
    db.commit()
    return db.query(models.ReportInfo).filter(models.ReportInfo.message_id == new_report.message_id).first()

def update_report_config(db: Session, old_report_config: schemas.ReportMainBase, new_report_config: schemas.ReportMainBase):
    if old_report_config == new_report_config:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_report_config.dict():
        if not new_report_config.__fields__[i]:
            new_report_config.__fields__[i] = old_report_config.__fields__[i]

    db_report_config = db.query(models.ReportMain).filter(models.ReportMain.guild_id == new_report_config.guild_id)
    db_report_config.update({**new_report_config.dict()})
    db.commit()
    return db.query(models.ReportMain).filter(models.ReportMain.guild_id == new_report_config.guild_id).first()

def update_autowelcomer_channels(db: Session, old_welcomer_channels: schemas.AutoWelcomerBase, new_welcomer_channels: schemas.AutoWelcomerBase):
    if old_welcomer_channels == new_welcomer_channels:
        raise HTTPException(
            status_code=status.HTTP_304_NOT_MODIFIED,
            detail="No update to data in database"
        )
    
    for i in new_welcomer_channels.dict():
        if not new_welcomer_channels.__fields__[i]:
            new_welcomer_channels.__fields__[i] = old_welcomer_channels.__fields__[i]

    db_report_config = db.query(models.ReportMain).filter(models.ReportMain.guild_id == new_welcomer_channels.guild_id)
    db_report_config.update({**new_welcomer_channels.dict()})
    db.commit()
    return db.query(models.ReportMain).filter(models.ReportMain.guild_id == new_welcomer_channels.guild_id).first()
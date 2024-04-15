import json
from typing import List
from sqlalchemy.orm import Session

from designs import models, schemas
import utils

def insert_guild_info(db: Session, guild: schemas.GuildMainBase):
    db_guild = models.GuildMain(**guild.dict())
    db.add(db_guild)
    db.commit()
    db.refresh(db_guild)
    return db_guild

def insert_guild_stats(db: Session, guild: schemas.ServerstatsMainBase):
    db_guild = models.ServerstatsMain(**guild.dict())
    db.add(db_guild)
    db.commit()
    db.refresh(db_guild)
    return db_guild

def insert_mod_main(db: Session, guild: schemas.ModerationMainBase):
    db_guild = models.ModerationMain(**guild.dict())
    db.add(db_guild)
    db.commit()
    db.refresh(db_guild)
    return db_guild

def insert_guild_mod_log(db: Session, mod_log: schemas.GuildModBase):
    db_mod_log = models.GuildMod(**mod_log.dict())
    db.add(db_mod_log)
    db.commit()
    db.refresh(db_mod_log)
    return db_mod_log

def insert_guild_logging_config(db: Session, guild: schemas.LoggingMainBase):
    guild.channel_channel_blacklist = str(guild.channel_channel_blacklist) if guild.channel_channel_blacklist else '[]'
    guild.role_role_blacklist = str(guild.role_role_blacklist) if guild.role_role_blacklist else '[]'

    db_guild = models.LoggingMain(**guild.dict())
    db.add(db_guild)
    db.commit()
    db.refresh(db_guild)

    db_guild.channel_channel_blacklist = json.loads(guild.channel_channel_blacklist)
    db_guild.role_role_blacklist = json.loads(guild.role_role_blacklist)

    return db_guild

def insert_auto_thread(db: Session, auto_thread: schemas.AutoThreadMainBase):
    db_auto_thread = models.AutoThreadMain(**auto_thread.dict())
    db.add(db_auto_thread)
    db.commit()
    db.refresh(db_auto_thread)
    return db_auto_thread

def insert_economy_player(db: Session, user: schemas.EconomyMainBase):
    db_user = models.EconomyMain(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def insert_private_voice_channel(db: Session, channel: schemas.VoiceChannelsBase):
    db_channel = models.VoiceChannels(**channel.dict())
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel

def insert_private_voice_channel_config(db: Session, channel: schemas.VoiceChannelsMainBase):
    db_channel = models.VoiceChannelsMain(**channel.dict())
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel

def insert_sticky_message(db: Session, sticky_message: schemas.StickyMainBase):
    db_sticky_message = models.StickyMain(**sticky_message.dict())
    db.add(db_sticky_message)
    db.commit()
    db.refresh(db_sticky_message)
    return db_sticky_message

def insert_ticket(db: Session, ticket: schemas.CurrentTicketsBase):
    db_ticket = models.CurrentTickets(**ticket.dict())
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    return db_ticket

def insert_ticket_config(db: Session, ticket_config: schemas.SupportMainBase):
    db_ticket_config = models.SupportMain(**ticket_config.dict())
    db.add(db_ticket_config)
    db.commit()
    db.refresh(db_ticket_config)
    return db_ticket_config

def insert_ticket_blacklist(db: Session, blacklist: schemas.TicketBlacklistsBase):
    db_blacklist = models.TicketBlacklists(**blacklist.dict())
    db.add(db_blacklist)
    db.commit()
    db.refresh(db_blacklist)
    return db_blacklist

def insert_giveaway(db: Session, giveaway: schemas.GiveawayMainBase):
    giveaway.entrants = str(giveaway.entrants) if giveaway.entrants else '[]'
    giveaway.allowedroles = str(giveaway.allowedroles) if giveaway.allowedroles else '[]'
    giveaway.blockedroles = str(giveaway.blockedroles) if giveaway.blockedroles else '[]'
    giveaway.bypassroles = str(giveaway.bypassroles) if giveaway.bypassroles else '[]'

    db_giveaway = models.GiveawayMain(**giveaway.dict())
    db.add(db_giveaway)
    db.commit()
    db.refresh(db_giveaway)

    db_giveaway.entrants = json.loads(db_giveaway.entrants)
    db_giveaway.allowedroles = json.loads(db_giveaway.allowedroles)
    db_giveaway.blockedroles = json.loads(db_giveaway.blockedroles)
    db_giveaway.bypassroles = json.loads(db_giveaway.bypassroles)
    return db_giveaway

def insert_giveaway_blocked(db: Session, giveaway_blocked: schemas.GiveawayBlockedBase):
    db_giveaway_blocked = models.GiveawayBlocked(**giveaway_blocked.dict())
    db.add(db_giveaway_blocked)
    db.commit()
    db.refresh(db_giveaway_blocked)
    return db_giveaway_blocked

def insert_giveaway_booster(db: Session, giveaway_booster: schemas.GiveawayBoostersBase):
    db_giveaway_booster = models.GiveawayBoosters(**giveaway_booster.dict())
    db.add(db_giveaway_booster)
    db.commit()
    db.refresh(db_giveaway_booster)
    return db_giveaway_booster

def insert_suggestion(db: Session, suggestion: schemas.SuggestionsMainBase):
    db_suggestion = models.SuggestionsMain(**suggestion.dict())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return db_suggestion

def insert_nickname_config(db: Session, nickname: schemas.NicknameMainBase):
    db_nickname = models.NicknameMain(**nickname.dict())
    db.add(db_nickname)
    db.commit()
    db.refresh(db_nickname)
    return db_nickname

def insert_nickname_request(db: Session, nickname_request: schemas.NicknameRequestsBase):
    db_nickname_request = models.NicknameMain(**nickname_request.dict())
    db.add(db_nickname_request)
    db.commit()
    db.refresh(db_nickname_request)
    return db_nickname_request

def insert_reaction_role(db: Session, reaction_role: schemas.NicknameRequestsBase):
    db_reaction_role = models.NicknameMain(**reaction_role.dict())
    db.add(db_reaction_role)
    db.commit()
    db.refresh(db_reaction_role)
    return db_reaction_role

def insert_autopublish_channels(db: Session, autopublish: schemas.AutopublishBase):
    db_autopublish = models.Autopublish(**autopublish.dict())
    db.add(db_autopublish)
    db.commit()
    db.refresh(db_autopublish)
    return db_autopublish

def insert_economy_user_settings(db: Session, economy_user: schemas.Economy_User_SettingsBase):
    db_economy_user = models.Economy_User_Settings(**economy_user.dict())
    db.add(db_economy_user)
    db.commit()
    db.refresh(db_economy_user)
    return db_economy_user

def insert_level_config(db: Session, level_config: schemas.Level_MainBase):
    db_level_config = models.Level_Main(**level_config.dict())
    db.add(db_level_config)
    db.commit()
    db.refresh(db_level_config)
    return db_level_config

def insert_level_roles(db: Session, level_roles: schemas.Level_RolesBase):
    db_level_roles = models.Level_Roles(**level_roles.dict())
    db.add(db_level_roles)
    db.commit()
    db.refresh(db_level_roles)
    return db_level_roles

def insert_level_user(db: Session, level_user: schemas.Level_UsersBase):
    db_level_user = models.Level_Users(**level_user.dict())
    db.add(db_level_user)
    db.commit()
    db.refresh(db_level_user)
    return db_level_user

def insert_notifications(db: Session, notification: schemas.NotificationsBase):
    db_notification = models.Notifications(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

def insert_suggestions_info(db: Session, suggestion: schemas.Suggestions_InfoBase):
    suggestion.upvotes = str(suggestion.upvotes) if suggestion.upvotes else '[]'
    suggestion.downvotes = str(suggestion.downvotes) if suggestion.downvotes else '[]'

    db_suggestion = models.Suggestions_Info(**suggestion.dict())
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)

    db_suggestion.upvotes = json.loads(db_suggestion.upvotes)
    db_suggestion.downvotes = json.loads(db_suggestion.downvotes)
    return db_suggestion

def insert_guild_aesthetics(db: Session, guild: schemas.Guild_Level_AestheticsBase):
    db_guild = models.Guild_Level_Aesthetics(**guild.dict())
    db.add(db_guild)
    db.commit()
    db.refresh(db_guild)
    return db_guild

def insert_application(db: Session, application: schemas.Application_QuestionsBase):
    data = application.copy()

    application.questions = "[" + ', '.join('&#39;' + i.replace("'", "\\'").replace('"', '\\"') + '&#39;' for i in application.questions) + "]"
    application.roles_required = str([i for i in application.roles_required]).replace("'", '"') if application.roles_required else '[]'

    db_application = models.Application_Questions(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)

    return data

def insert_application_response(db: Session, response: schemas.Application_AnswersBase):
    data = response.copy()

    response.q_a = "{" + ', '.join('&#39;' + i.replace("'", "\\'").replace('"', '\\"') + '&#39;: ' + '&#39;' + response.q_a[i].replace("'", "\\'").replace('"', '\\"') + '&#39;' for i in response.q_a) + "}"

    db_response = models.Application_Answers(**response.dict())
    db.add(db_response)
    db.commit()
    db.refresh(db_response)

    return data

def insert_level_boost_role(db: Session, role: schemas.Level_Bonus_RolesBase):
    db_role = models.Level_Bonus_Roles(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def insert_level_boost_channel(db: Session, channel: schemas.Level_Bonus_ChannelsBase):
    db_channel = models.Level_Bonus_Channels(**channel.dict())
    db.add(db_channel)
    db.commit()
    db.refresh(db_channel)
    return db_channel

def insert_reminder(db: Session, reminder: schemas.RemindersBase):
    db_reminder = models.Reminders(**reminder.dict())
    db.add(db_reminder)
    db.commit()
    db.refresh(db_reminder)
    return db_reminder

def insert_user_statistics(db: Session, user_statistics: schemas.UserStatisticsBase):
    db_user_statistics = models.UserStatistics(**user_statistics.dict())
    db.add(db_user_statistics)
    db.commit()
    db.refresh(db_user_statistics)
    return db_user_statistics

def insert_temp_giveaway_booster(db: Session, temp_giveaway_booster: schemas.GiveawayTempBoostersBase):
    db_temp_giveaway_booster = models.GiveawayTempBoosters(**temp_giveaway_booster.dict())
    db.add(db_temp_giveaway_booster)
    db.commit()
    db.refresh(db_temp_giveaway_booster)
    return db_temp_giveaway_booster

def insert_report(db: Session, report: schemas.ReportInfoBase):
    db_report = models.ReportInfo(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def insert_report_config(db: Session, report_config: schemas.ReportMainBase):
    db_report_config = models.ReportMain(**report_config.dict())
    db.add(db_report_config)
    db.commit()
    db.refresh(db_report_config)
    return db_report_config
from typing import List
from sqlalchemy.orm import Session

from designs import models, schemas

def delete_data(db: Session, item):
    db.delete(item)
    db.commit()

def delete_guild_info(db: Session, guild: schemas.GuildMainBase):
    delete_data(db, guild)

def delete_guild_stats(db: Session, guild: schemas.ServerstatsMainBase):
    delete_data(db, guild)

def delete_mod_main(db: Session, mod: schemas.ModerationMainBase):
    delete_data(db, mod)

def delete_guild_modlog(db: Session, mod_log: schemas.GuildModBase):
    delete_data(db, mod_log)

def delete_guild_log_config(db: Session, guild: schemas.LoggingMainBase):
    delete_data(db, guild)

def delete_auto_thread_detail(db: Session, auto_thread: schemas.AutoThreadMainBase):
    delete_data(db, auto_thread)

def delete_economy_user_detail(db: Session, user: schemas.EconomyMainBase):
    delete_data(db, user)

def delete_private_voice_channel_detail(db: Session, channel: schemas.VoiceChannelsBase):
    delete_data(db, channel)

def delete_private_voice_channel_config_detail(db: Session, channel: schemas.VoiceChannelsMainBase):
    delete_data(db, channel)

def delete_sticky_message_detail(db: Session, sticky_message: schemas.StickyMainBase):
    delete_data(db, sticky_message)

def delete_ticket_detail(db: Session, ticket: schemas.CurrentTicketsBase):
    delete_data(db, ticket)

def delete_ticket_config_detail(db: Session, ticket_config: schemas.SupportMainBase):
    delete_data(db, ticket_config)

def delete_ticket_blacklist(db: Session, blacklist: schemas.TicketBlacklistsBase):
    delete_data(db, blacklist)

def delete_giveaway(db: Session, giveaway: schemas.GiveawayMainBase):
    delete_data(db, giveaway)

def delete_giveaway_blocked(db: Session, giveaway_blocked: schemas.GiveawayBlockedBase):
    delete_data(db, giveaway_blocked)

def delete_giveaway_booster(db: Session, giveaway_booster: schemas.GiveawayBoostersBase):
    delete_data(db, giveaway_booster)

def delete_suggestion_channel(db: Session, suggestion_channel: schemas.SuggestionsMainBase):
    delete_data(db, suggestion_channel)

def delete_nickname_main(db: Session, nickname_main: schemas.NicknameMainBase):
    delete_data(db, nickname_main)

def delete_nickname_request(db: Session, nickname_request: schemas.NicknameRequestsBase):
    delete_data(db, nickname_request)

def delete_reaction_roles(db: Session, reaction_roles: schemas.ReactionMainBase):
    delete_data(db, reaction_roles)

def delete_autopublish_channels(db: Session, autopublish: schemas.AutopublishBase):
    delete_data(db, autopublish)

def delete_economy_user_settings(db: Session, economy_user: schemas.Economy_User_SettingsBase):
    delete_data(db, economy_user)

def delete_level_config(db: Session, level_config: schemas.Level_MainBase):
    delete_data(db, level_config)

def delete_level_roles(db: Session, level_role: schemas.Level_RolesBase):
    delete_data(db, level_role)

def delete_level_user(db: Session, level_user: schemas.Level_UsersBase):
    delete_data(db, level_user)

def delete_notifications(db: Session, notification: schemas.NotificationsBase):
    delete_data(db, notification)

def delete_suggestions_info(db: Session, suggestion: schemas.Suggestions_InfoBase):
    delete_data(db, suggestion)

def delete_guild_aesthetics(db: Session, guild: schemas.Guild_Level_AestheticsBase):
    delete_data(db, guild)

def delete_application(db: Session, application: schemas.Application_QuestionsBase):
    delete_data(db, application)

def delete_application_response(db: Session, response: schemas.Application_AnswersBase):
    delete_data(db, response)

def delete_level_bonus_role(db: Session, role: schemas.Level_Bonus_RolesBase):
    delete_data(db, role)

def delete_level_bonus_channel(db: Session, channel: schemas.Level_Bonus_ChannelsBase):
    delete_data(db, channel)

def delete_reminder(db: Session, reminder: schemas.RemindersBase):
    delete_data(db, reminder)

def delete_user_statistics(db: Session, user_statistics: schemas.UserStatisticsBase):
    delete_data(db, user_statistics)

def delete_giveaway_temp_boosters(db: Session, temp_giveaway_booster: schemas.GiveawayTempBoostersBase):
    delete_data(db, temp_giveaway_booster)

def delete_report(db: Session, report: schemas.ReportInfoBase):
    delete_data(db, report)

def delete_report_config(db: Session, report_config: schemas.ReportMainBase):
    delete_data(db, report_config)

def delete_autowelcomer_channels(db: Session, autowelcomer: schemas.AutoWelcomerBase):
    delete_data(db, autowelcomer)
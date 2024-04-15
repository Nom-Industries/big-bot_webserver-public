import json
from typing import List
from sqlalchemy.orm import Session

from designs import models, schemas
import utils

def get_guild_info(db: Session, query: dict) -> List[schemas.GuildMainBase]:
    result: List[schemas.GuildMainBase] = db.query(models.GuildMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.GuildMainBase) if result else None

def get_guild_stats(db: Session, query: dict) -> List[schemas.ServerstatsMainBase]:
    result: List[schemas.ServerstatsMainBase] = db.query(models.ServerstatsMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.ServerstatsMainBase) if result else None

def get_guild_mod_data(db: Session, query: dict) -> List[schemas.GuildModBase]:
    result: List[schemas.GuildModBase] = db.query(models.GuildMod).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.GuildModBase) if result else None

def get_mod_main(db: Session, query: dict) -> List[schemas.ModerationMainBase]:
    result: List[schemas.ModerationMainBase] = db.query(models.ModerationMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.ModerationMainBase) if result else None

def get_guild_logging_config(db: Session, query: dict) -> List[schemas.LoggingMainBase]:
    if "channel_channel_blacklist" in query:
        query["channel_channel_blacklist"] = str(query["channel_channel_blacklist"])

    if "role_role_blacklist" in query:
        query["role_role_blacklist"] = str(query["role_role_blacklist"])

    result: List[schemas.LoggingMainBase] = db.query(models.LoggingMain).filter_by(**query).all()

    if not result:
        return None
    
    for i in range(len(result)):
        result[i].channel_channel_blacklist = json.loads(result[i].channel_channel_blacklist)
        result[i].role_role_blacklist = json.loads(result[i].role_role_blacklist)

    return utils.convert_data_values(result, schemas.LoggingMainBase) if result else None

def get_economy_info(db: Session, query: dict) -> List[schemas.EconomyMainBase]:
    result: List[schemas.EconomyMainBase] = db.query(models.EconomyMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.EconomyMainBase) if result else None

def get_current_tickets(db: Session, query: dict) -> List[schemas.CurrentTicketsBase]:
    result: List[schemas.CurrentTicketsBase] = db.query(models.CurrentTickets).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.CurrentTicketsBase) if result else None

def get_auto_thread_info(db: Session, query: dict) -> List[schemas.AutoThreadMainBase]:
    result: List[schemas.AutoThreadMainBase] = db.query(models.AutoThreadMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.AutoThreadMainBase) if result else None

def get_sticky_message_info(db: Session, query: dict) -> List[schemas.StickyMainBase]:
    result: List[schemas.StickyMainBase] = db.query(models.StickyMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.StickyMainBase) if result else None

def get_support_data(db: Session, query: dict) -> List[schemas.SupportMainBase]:
    result: List[schemas.SupportMainBase] = db.query(models.SupportMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.SupportMainBase) if result else None

def get_priv_voice_channels(db: Session, query: dict) -> List[schemas.VoiceChannelsBase]:
    result: List[schemas.VoiceChannelsBase] = db.query(models.VoiceChannels).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.VoiceChannelsBase) if result else None

def get_priv_voice_channel_config(db: Session, query: dict) -> List[schemas.VoiceChannelsMainBase]:
    result: List[schemas.VoiceChannelsMainBase] = db.query(models.VoiceChannelsMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.VoiceChannelsMainBase) if result else None

def get_ticket_blacklists(db: Session, query: dict) -> List[schemas.TicketBlacklistsBase]:
    result: List[schemas.TicketBlacklistsBase] = db.query(models.TicketBlacklists).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.TicketBlacklistsBase) if result else None

def get_giveaways(db: Session, query: dict) -> List[schemas.GiveawayMainBase]:
    result: List[schemas.GiveawayMainBase] = db.query(models.GiveawayMain).filter_by(**query).all()

    if not result:
        return None

    for i in range(len(result)):
        result[i].entrants = json.loads(result[i].entrants) if result[i].entrants else []
        result[i].allowedroles = json.loads(result[i].allowedroles) if result[i].allowedroles and "[" in result[i].allowedroles else [] if not result[i].allowedroles else [int(j) for j in result[i].allowedroles.replace(" ", "").split(",")]
        result[i].blockedroles = json.loads(result[i].blockedroles) if result[i].blockedroles and "[" in result[i].blockedroles else [] if not result[i].blockedroles else [int(j) for j in result[i].blockedroles.replace(" ", "").split(",")]
        result[i].bypassroles = json.loads(result[i].bypassroles) if result[i].bypassroles and "[" in result[i].bypassroles else [] if not result[i].bypassroles else [int(j) for j in result[i].bypassroles.replace(" ", "").split(",")]

    return result

def get_giveaway_blocked(db: Session, query: dict) -> List[schemas.GiveawayBlockedBase]:
    result: List[schemas.GiveawayBlockedBase] = db.query(models.GiveawayBlocked).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.GiveawayBlockedBase) if result else None

def get_giveaway_boosters(db: Session, query: dict) -> List[schemas.GiveawayBoostersBase]:
    result: List[schemas.GiveawayBoostersBase] = db.query(models.GiveawayBoosters).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.GiveawayBoostersBase) if result else None

def get_suggestions_channel(db: Session, query: dict) -> List[schemas.SuggestionsMainBase]:
    result: List[schemas.SuggestionsMainBase] = db.query(models.SuggestionsMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.SuggestionsMainBase) if result else None

def get_nickname_main(db: Session, query: dict) -> List[schemas.NicknameMainBase]:
    result: List[schemas.NicknameMainBase] = db.query(models.NicknameMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.NicknameMainBase) if result else None

def get_nickname_requests(db: Session, query: dict) -> List[schemas.NicknameRequestsBase]:
    result: List[schemas.NicknameRequestsBase] = db.query(models.NicknameRequests).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.NicknameRequestsBase) if result else None

def get_reaction_roles(db: Session, query: dict) -> List[schemas.ReactionMainBase]:
    result: List[schemas.ReactionMainBase] = db.query(models.ReactionMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.ReactionMainBase) if result else None

def get_autopublish_channels(db: Session, query: dict) -> List[schemas.AutopublishBase]:
    result: List[schemas.AutopublishBase] = db.query(models.Autopublish).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.AutopublishBase) if result else None

def get_economy_user_settings(db: Session, query: dict) -> List[schemas.Economy_User_SettingsBase]:
    result: List[schemas.Economy_User_SettingsBase] = db.query(models.Economy_User_Settings).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.Economy_User_SettingsBase) if result else None

def get_level_config(db: Session, query: dict) -> List[schemas.Level_MainBase]:
    result: List[schemas.Level_MainBase] = db.query(models.Level_Main).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.Level_MainBase) if result else None

def get_level_roles(db: Session, query: dict) -> List[schemas.Level_RolesBase]:
    result: List[schemas.Level_RolesBase] = db.query(models.Level_Roles).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.Level_RolesBase) if result else None

def get_level_user(db: Session, query: dict) -> List[schemas.Level_UsersBase]:
    result: List[schemas.Level_UsersBase] = db.query(models.Level_Users).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.Level_UsersBase) if result else None

def get_notifications(db: Session, query: dict) -> List[schemas.NotificationsBase]:
    result: List[schemas.NotificationsBase] = db.query(models.Notifications).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.NotificationsBase) if result else None

def get_suggestions_info(db: Session, query: dict) -> List[schemas.Suggestions_InfoBase]:
    result: List[schemas.Suggestions_InfoBase] = db.query(models.Suggestions_Info).filter_by(**query).all()

    result = utils.convert_data_values(result, schemas.Suggestions_InfoBase) if result else None

    if result == None:
        return result

    for i in range(len(result)):
        result[i].upvotes = json.loads(result[i].upvotes)
        result[i].downvotes = json.loads(result[i].downvotes)

    return result

def get_guild_aesthetics(db: Session, query: dict) -> List[schemas.Guild_Level_AestheticsBase]:
    result: List[schemas.Guild_Level_AestheticsBase] = db.query(models.Guild_Level_Aesthetics).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.Guild_Level_AestheticsBase) if result else None

def get_applications(db: Session, query: dict) -> List[schemas.Application_QuestionsBase]:
    if "roles_required" in query:
        query["roles_required"] = str([i for i in query["roles_required"]]).replace("'", '"')
    
    if "enabled" in query:
        query["enabled"] = 1 if query["enabled"] else 0
    
    result: List[schemas.Application_QuestionsBase] = db.query(models.Application_Questions).filter_by(**query).all()

    result = utils.convert_data_values(result, schemas.Application_QuestionsBase) if result else None

    if not result:
        return None
    
    for i in range(len(result)):
        result[i].questions = json.loads(result[i].questions.replace("\\\\'", "'").replace('"', '\\"').replace("&#39;", '\"'))
        result[i].roles_required = json.loads(result[i].roles_required) if result[i].roles_required else []
    
    return result

def get_application_responses(db: Session, query: dict) -> List[schemas.Application_AnswersBase]:
    result: List[schemas.Application_AnswersBase] = db.query(models.Application_Answers).filter_by(**query).all()

    result = utils.convert_data_values(result, schemas.Application_AnswersBase) if result else None
    
    if not result:
        return None

    for i in range(len(result)):
        result[i].q_a = json.loads(result[i].q_a.replace("\\\\'", "'").replace('"', '\\"').replace("&#39;", '\"'))
    
    return result

def get_level_bonus_roles(db: Session, query: dict) -> List[schemas.Level_Bonus_RolesBase]:
    result: List[schemas.Level_Bonus_RolesBase] = db.query(models.Level_Bonus_Roles).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.Level_Bonus_RolesBase) if result else None

def get_level_bonus_channels(db: Session, query: dict) -> List[schemas.Level_Bonus_ChannelsBase]:
    result: List[schemas.Level_Bonus_ChannelsBase] = db.query(models.Level_Bonus_Channels).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.Level_Bonus_ChannelsBase) if result else None

def get_reminders(db: Session, query: dict) -> List[schemas.RemindersBase]:
    result: List[schemas.RemindersBase] = db.query(models.Reminders).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.RemindersBase) if result else None

def get_user_statistics(db: Session, query: dict) -> List[schemas.UserStatisticsBase]:
    result: List[schemas.UserStatisticsBase] = db.query(models.UserStatistics).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.UserStatisticsBase) if result else None

def get_giveaway_temp_boosters(db: Session, query: dict) -> List[schemas.GiveawayTempBoostersBase]:
    result: List[schemas.GiveawayTempBoostersBase] = db.query(models.GiveawayTempBoosters).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.GiveawayTempBoostersBase) if result else None

def get_reports(db: Session, query: dict) -> List[schemas.ReportInfoBase]:
    result: List[schemas.ReportInfoBase] = db.query(models.ReportInfo).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.ReportInfoBase) if result else None

def get_report_config(db: Session, query: dict) -> List[schemas.ReportMainBase]:
    result: List[schemas.ReportMainBase] = db.query(models.ReportMain).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.ReportMainBase) if result else None

def get_autowelcomer_channels(db: Session, query: dict) -> List[schemas.AutoWelcomerBase]:
    result: List[schemas.AutoWelcomerBase] = db.query(models.Autowelcomer).filter_by(**query).all()

    return utils.convert_data_values(result, schemas.AutoWelcomerBase) if result else None

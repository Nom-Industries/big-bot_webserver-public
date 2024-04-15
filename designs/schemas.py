from typing import List, Dict, Optional, Union
from pydantic import BaseModel
from database.database import Base

class Table(BaseModel):
    def __eq__(self, other: Base):
        equal = True

        for i in self.__fields__:
            if (self.dict()[i] or other.__dict__[i]) and self.dict()[i] != other.__dict__[i]:
                return False
        
        return equal

class GuildMainBase(Table):
    guild_id: int
    welcome_channel: Optional[int]
    log_channel: Optional[str]
    autorole_ids: Optional[str]
    welcome_msg: Optional[str]
    auto_thread_channels: Optional[str]

    class Config:
        orm_mode = True
    
class ServerstatsMainBase(Table):
    guild_id: int
    channel_id: int
    type: str
    
    class Config:
        orm_mode = True

class GuildModBase(Table):
    guild_id: int
    punishment_id: str
    member_id: int
    mod_id: int
    type: str
    reason: Optional[str]
    duration: Union[int, str]
    expired: Optional[str]
    expires: Union[int, str]
    given: int
    evidence: Optional[str]

    class Config:
        orm_mode = True

class GuildModBaseModify(GuildModBase):
    guild_id: Optional[int]
    punishment_id: str
    member_id: Optional[int]
    mod_id: Optional[int]
    type: Optional[str]
    reason: Optional[str]
    duration: Optional[Union[int, str]]
    expires: Optional[Union[int, str]]

class ModerationMainBase(Table):
    guild: int
    muted_role: Optional[int]
    mod_log_channel: Optional[int]

    class Config:
        orm_mode = True

class LoggingMainBase(Table):
    guild_id: int
    webhook_link: Optional[str]
    channel_id: Optional[Union[int, str]]
    message: Optional[bool] = None
    role: Optional[bool] = None
    member: Optional[bool] = None
    voice: Optional[bool] = None
    channel: Optional[bool] = None
    invite: Optional[bool] = None
    user: Optional[bool] = None
    channel_channel_blacklist: Optional[List[int]]
    role_role_blacklist: Optional[List[int]] = None

    class Config:
        orm_mode = True

class EconomyMainBase(Table):
    user_id: int
    guild_id: str
    balance: int
    daily: int
    weekly: int
    monthly: int
    spear: Optional[int] = 0
    rifle: Optional[int] = 0
    minion: Optional[int] = 0
    lucky_pet: Optional[str] = 0
    booster_pet: Optional[str] = 0
    current_boost: Optional[float] = 1
    p_trophy: Optional[int] = 0
    r_trophy: Optional[int] = 0
    sr_trophy: Optional[int] = 0
    smr_trophy: Optional[int] = 0
    simr_trophy: Optional[int] = 0
    rod: Optional[int] = 0
    comp: Optional[int] = 0
    norm_boost: Optional[int] = 0
    job: Optional[str] = 0
    bait: Optional[int] = 0
    minion_last_check: Optional[int] = 0
    minion_full: Optional[int] = 0
    yeast: Optional[int] = 0
    pedestal: Optional[int] = 0
    energy: Optional[int] = 0
    poison: Optional[int] = 0
    spade: Optional[int] = 0
    drill: Optional[int] = 0

    class Config:
        orm_mode = True

class CurrentTicketsBase(Table):
    channel_id: int
    author_id: int
    originmessage_id: int

    class Config:
        orm_mode = True

class AutoThreadMainBase(Table):
    guild_id: int
    channel_id: int

    class Config:
        orm_mode = True

class StickyMainBase(Table):
    guild_id: int
    channel_id: int
    message_id: int
    message: str
    title: Optional[str]
    description: Optional[str]
    type: str

    class Config:
        orm_mode = True

class SupportMainBase(Table):
    guild_id: int
    message_id: int
    supportrole_id: Optional[int]
    supportcategory_id: Optional[int]
    creation_message: str
    pingrole_id: Optional[int]
    logchannel_id: Optional[int]
    dmonclose: Optional[bool]

    class Config:
        orm_mode = True
    
class TicketBlacklistsBase(Table):
    member: int
    guild: int
    moderator: int
    reason: str
    given: int

    class Config:
        orm_mode = True

class VoiceChannelsBase(Table):
    guild_id: int
    owner_id: int
    private: str
    channel_id: int
    base_call_id: int
    request_join_id: int = None
    request_join_text_id: int = None

    class Config:
        orm_mode = True

class VoiceChannelsMainBase(Table):
    guild_id: int
    channel_id: int
    name: str
    logchannel: int

    class Config:
        orm_mode = True

class GiveawayMainBase(Table):
    guild_id: int
    channel_id: int
    message_id: int
    winners: int
    item: str
    ends: int
    entrants: Optional[Union[List[int], str]] = None
    allowedroles: Optional[Union[List[int], str]] = None
    blockedroles: Optional[Union[List[int], str]] = None
    boostedroles: Optional[Dict[str, int]] = None
    stackboostedroles: Optional[bool] = False
    min_daily_msgs: Optional[int] = 0
    min_weekly_msgs: Optional[int] = 0
    min_monthly_msgs: Optional[int] = 0
    min_total_msgs: Optional[int] = 0
    bypassroles: Optional[Union[List[int], str]] = None

    class Config:
        orm_mode = True

class GiveawayBlockedBase(Table):
    role_id: int
    guild_id: int

    class Config:
        orm_mode = True

class GiveawayBoostersBase(Table):
    role_id: int
    guild_id: int
    boost: int
    
    class Config:
        orm_mode = True

class SuggestionsMainBase(Table):
    guild_id: int
    channel_id: int
    type: str
    autothread: int
    send: Optional[str]
    accept_channel: Optional[int]
    deny_channel: Optional[int]

    class Config:
        orm_mode = True

class NicknameMainBase(Table):
    guild_id: int
    channel_id: int
    mod_role_id: Optional[int]
    required_role: Optional[int]

    class Config:
        orm_mode = True

class NicknameRequestsBase(Table):
    guild: int
    requested_nick: str
    user: int
    message_id: int
    channel_sent_id: int

    class Config:
        orm_mode = True

class ReactionMainBase(Table):
    guild_id: int
    message_id: int
    channel_id: int
    reaction_type: str
    message_type: int
    roles: str

    class Config:
        orm_mode = True

class AutopublishBase(Table):
    guild_id: int
    channel_id: int

    class Config:
        orm_mode = True

class Economy_User_SettingsBase(Table):
    user: int
    tips: bool

    class Config:
        orm_mode = True

class Level_MainBase(Table):
    guild_id: int
    enabled: bool = True
    min_xp: int = 10
    max_xp: int = 15
    min_vc_xp: int = 5
    max_vc_xp: int = 10
    level_up_message: Optional[str] = None
    level_up_channel: Optional[str] = None
    drops: bool = False
    background_color: Optional[str] = None
    main_color: Optional[str] = None
    primary_font_color: Optional[str] = None
    secondary_font_color: Optional[str] = None
    no_xp_channels: Optional[Union[str, List[int]]] = None
    no_xp_roles: Optional[Union[str, List[int]]] = None
    stackable_rewards: bool = False
    cooldown: Optional[int] = None
    reward_message: Optional[str] = None
    max_level: Optional[int] = None
    voice_xp_gain: bool = False
    mee6_levels: Optional[bool] = False
        
    class Config:
        orm_mode = True

class Level_RolesBase(Table):
    guild_id: int
    level: int
    role_id: int

    class Config:
        orm_mode = True

class Level_UsersBase(Table):
    unique_id: str
    guild_id: int
    user_id: int
    total_xp: int
    background_color: Optional[str] = None
    main_color: Optional[str] = None
    primary_font_color: Optional[str] = None
    secondary_font_color: Optional[str] = None
    last_xp_gain: Optional[int] = None

    class Config:
        orm_mode = True

class NotificationsBase(Table):
    channel_id: int
    guild_id: int
    ping_channel_id: int
    ping_message: str
    type: str

    class Config:
        orm_mode = True

class Suggestions_InfoBase(Table):
    suggestion_id: str
    guild_id: int
    channel_id: int
    message_id: int
    user_id: int
    status: str = "Pending"
    upvotes: List[int]
    downvotes: List[int]

    class Config:
        orm_mode = True

class Guild_Level_AestheticsBase(Table):
    guild_id: int
    background_color: Optional[str] = None
    main_color: Optional[str] = None
    primary_font_color: Optional[str] = None
    secondary_font_color: Optional[str] = None

    class Config:
        orm_mode = True

class Application_QuestionsBase(Table):
    app_id: str
    guild_id: int
    name: str
    questions: List[str]
    channel_to_send: int
    enabled: bool = True
    roles_required: Optional[List[int]] = None
    category: Optional[int] = None

    class Config:
        orm_mode = True

class Application_AnswersBase(Table):
    app_id: str
    guild_id: int
    user_id: int
    app_name: str
    q_a: Dict[str, str]
    verdict: Optional[bool] = None
    reason: Optional[str] = None
    mod_id: Optional[int] = None
    channel_id: Optional[int] = None

    class Config:
        orm_mode = True

class Level_Bonus_RolesBase(Table):
    guild_id: int
    role_id: int
    boost: int

    class Config:
        orm_mode = True

class Level_Bonus_ChannelsBase(Table):
    guild_id: int
    channel_id: int
    boost: int

    class Config:
        orm_mode = True

class RemindersBase(Table):
    reminder_id: str
    guild_id: int
    channel_id: int
    user_id: int
    message: str
    time: int
    completed: bool
    
    class Config:
        orm_mode = True

class UserStatisticsBase(Table):
    unique_id: str
    guild_id: int
    user_id: int
    total_msgs: int = 0
    last_daily_msgs: int = 0
    last_weekly_msgs: int = 0
    last_monthly_msgs: int = 0

    class Config:
        orm_mode = True

class GiveawayTempBoostersBase(Table):
    unique_id: Optional[str]
    message_id: int
    boost_role_id: int
    boost_amount: int

    class Config:
        orm_mode = True

class ReportInfoBase(Table):
    guild_id: int
    message_id: int
    reporter_id: int
    reported_id: int
    verdict: Optional[str]
    verdict_id: Optional[int]
    verdict_message: Optional[str]

    class Config:
        orm_mode = True

class ReportMainBase(Table):
    guild_id: int
    channel_id: int
    required_role: int
    ping_role: int
    mod_role: int
    
    class Config:
        orm_mode = True

class AutoWelcomerBase(Table):
    guild_id: int
    welcome_channel_id: Optional[int]
    image: Optional[bool] = True
    welcome_message: Optional[str] = "Welcome **{$user_name}** to the **{$guild_name}**. You are our {$guild_member_count_formatted} member!"

    class Config:
        orm_mode=True
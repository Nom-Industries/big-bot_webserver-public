from database.database import Base
from sqlalchemy import Column, Text, Boolean

class GuildMain(Base):
    __tablename__ = 'guild_main'

    guild_id = Column(Text, primary_key=True)
    welcome_channel = Column(Text)
    log_channel = Column(Text)
    autorole_ids = Column(Text)
    welcome_msg = Column(Text)
    auto_thread_channels = Column(Text)

class GuildMod(Base):
    __tablename__ = 'guild_mod'

    guild_id = Column(Text)
    punishment_id = Column(Text, primary_key=True)
    member_id = Column(Text)
    mod_id = Column(Text)
    type = Column(Text)
    reason = Column(Text)
    duration = Column(Text)
    expired = Column(Text)
    expires = Column(Text)
    given = Column(Text)
    evidence = Column(Text)

class ModerationMain(Base):
    __tablename__ = 'moderation_main'

    guild = Column(Text, primary_key=True)
    muted_role = Column(Text)
    mod_log_channel = Column(Text)

class LoggingMain(Base):
    __tablename__ = 'logging_main'

    guild_id = Column(Text)
    message = Column(Text)
    role = Column(Text)
    member = Column(Text)
    voice = Column(Text)
    channel = Column(Text)
    invite = Column(Text)
    user = Column(Text)
    webhook_link = Column(Text, primary_key=True)
    channel_id = Column(Text)
    channel_channel_blacklist = Column(Text)
    role_role_blacklist = Column(Text)

class EconomyMain(Base):
    __tablename__ = 'economy_main'

    user_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    balance = Column(Text)
    daily = Column(Text)
    weekly = Column(Text)
    monthly = Column(Text)
    spear = Column(Text)
    rifle = Column(Text)
    minion = Column(Text)
    lucky_pet = Column(Text)
    booster_pet = Column(Text)
    current_boost = Column(Text)
    p_trophy = Column(Text)
    r_trophy = Column(Text)
    sr_trophy = Column(Text)
    smr_trophy = Column(Text)
    simr_trophy = Column(Text)
    rod = Column(Text)
    comp = Column(Text)
    norm_boost = Column(Text)
    job = Column(Text)
    bait = Column(Text)
    minion_last_check = Column(Text)
    minion_full = Column(Text)
    yeast = Column(Text)
    pedestal = Column(Text)
    energy = Column(Text)
    poison = Column(Text)
    spade = Column(Text)
    drill = Column(Text)

class CurrentTickets(Base):
    __tablename__ = 'current_tickets'

    channel_id = Column(Text, primary_key=True)
    author_id = Column(Text)
    originmessage_id = Column(Text)

class AutoThreadMain(Base):
    __tablename__ = 'autothread_main'

    guild_id = Column(Text)
    channel_id = Column(Text, primary_key=True)

class StickyMain(Base):
    __tablename__ = 'sticky_main'

    guild_id = Column(Text)
    channel_id = Column(Text, primary_key=True)
    message_id = Column(Text)
    message = Column(Text)
    title = Column(Text)
    description = Column(Text)
    type = Column(Text)

class SupportMain(Base):
    __tablename__ = 'support_main'

    guild_id = Column(Text)
    message_id = Column(Text, primary_key=True)
    supportrole_id = Column(Text)
    supportcategory_id = Column(Text)
    creation_message = Column(Text)
    pingrole_id = Column(Text)
    logchannel_id = Column(Text)
    dmonclose = Column(Boolean)

class VoiceChannels(Base):
    __tablename__ = 'voice_channels'

    guild_id = Column(Text)
    owner_id = Column(Text)
    private = Column(Text)
    channel_id = Column(Text, primary_key=True)
    base_call_id = Column(Text)
    request_join_id = Column(Text)
    request_join_text_id = Column(Text)

class VoiceChannelsMain(Base):
    __tablename__ = 'voice_channels_main'

    guild_id = Column(Text)
    channel_id = Column(Text, primary_key=True)
    name = Column(Text)
    logchannel = Column(Text)

class GiveawayMain(Base):
    __tablename__ = 'giveaway_main'

    guild_id = Column(Text)
    channel_id = Column(Text)
    message_id = Column(Text, primary_key=True)
    winners = Column(Text)
    item = Column(Text)
    ends = Column(Text)
    entrants = Column(Text)
    allowedroles = Column(Text)
    blockedroles = Column(Text)
    boostedroles = Column(Text)
    stackboostedroles = Column(Boolean)
    min_daily_msgs = Column(Text)
    min_weekly_msgs = Column(Text)
    min_monthly_msgs = Column(Text)
    min_total_msgs = Column(Text)
    bypassroles = Column(Text)

class GiveawayBlocked(Base):
    __tablename__ = 'giveaway_blocked'

    role_id = Column(Text, primary_key=True)
    guild_id = Column(Text)

class GiveawayBoosters(Base):
    __tablename__ = 'giveaway_boosters'

    role_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    boost = Column(Text)

class ServerstatsMain(Base):
    __tablename__ = 'serverstats_main'

    guild_id = Column(Text)
    channel_id = Column(Text, primary_key=True)
    type = Column(Text)

class SuggestionsMain(Base):
    __tablename__ = 'suggestions_main'

    guild_id = Column(Text)
    channel_id = Column(Text, primary_key=True)
    type = Column(Text)
    autothread = Column(Text)
    send = Column(Text)
    accept_channel = Column(Text)
    deny_channel = Column(Text)

class TicketBlacklists(Base):
    __tablename__ = 'ticket_blacklists'

    member = Column(Text, primary_key=True)
    guild = Column(Text)
    moderator = Column(Text)
    reason = Column(Text)
    given = Column(Text)

class NicknameMain(Base):
    __tablename__ = "nickname_main"

    guild_id = Column(Text, primary_key=True)
    channel_id = Column(Text)
    mod_role_id = Column(Text)
    required_role = Column(Text)

class NicknameRequests(Base):
    __tablename__ = "nickname_requests"

    guild = Column(Text)
    requested_nick = Column(Text)
    user = Column(Text)
    message_id = Column(Text, primary_key=True)
    channel_sent_id = Column(Text)

class ReactionMain(Base):
    __tablename__ = "reaction_main"

    guild_id = Column(Text)
    message_id = Column(Text, primary_key=True)
    channel_id = Column(Text)
    reaction_type = Column(Text)
    message_type = Column(Text)
    roles = Column(Text)

class Autopublish(Base):
    __tablename__ = "autopublish"

    guild_id = Column(Text)
    channel_id = Column(Text, primary_key=True)

class Economy_User_Settings(Base):
    __tablename__ = "economy_user_settings"

    user = Column(Text, primary_key=True)
    tips = Column(Text)

class Level_Main(Base):
    __tablename__ = "level_main"

    guild_id = Column(Text, primary_key=True)
    enabled = Column(Text, default=True)
    min_xp = Column(Text, default=10)
    max_xp = Column(Text, default=15)
    min_vc_xp = Column(Text, default=5)
    max_vc_xp = Column(Text, default=10)
    level_up_message = Column(Text)
    level_up_channel = Column(Text)
    drops = Column(Text)
    background_color = Column(Text)
    main_color = Column(Text)
    primary_font_color = Column(Text)
    secondary_font_color = Column(Text)
    no_xp_channels = Column(Text)
    no_xp_roles = Column(Text)
    stackable_rewards = Column(Text, default=True)
    cooldown = Column(Text)
    reward_message = Column(Text)
    max_level = Column(Text)
    voice_xp_gain = Column(Text, default=True)
    mee6_levels = Column(Text, default=False)

class Level_Roles(Base):
    __tablename__ = "level_roles"

    guild_id = Column(Text)
    level = Column(Text)
    role_id = Column(Text, primary_key=True)

class Level_Users(Base):
    __tablename__ = "level_users"

    unique_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    user_id = Column(Text)
    total_xp = Column(Text)
    background_color = Column(Text)
    main_color = Column(Text)
    primary_font_color = Column(Text)
    secondary_font_color = Column(Text)
    voice_minutes = Column(Text)
    last_xp_gain = Column(Text)

class Notifications(Base):
    __tablename__ = "notifications"

    channel_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    ping_channel_id = Column(Text)
    ping_message = Column(Text)
    type = Column(Text)

class Suggestions_Info(Base):
    __tablename__ = "suggestions_info"

    suggestion_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    channel_id = Column(Text)
    message_id = Column(Text)
    user_id = Column(Text)
    status = Column(Text, default="Pending")
    upvotes = Column(Text)
    downvotes = Column(Text)

class Guild_Level_Aesthetics(Base):
    __tablename__ = "guild_level_aesthetics"

    guild_id = Column(Text, primary_key=True)
    background_color = Column(Text)
    main_color = Column(Text)
    primary_font_color = Column(Text)
    secondary_font_color = Column(Text)

class Application_Questions(Base):
    __tablename__ = "application_questions"

    app_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    name = Column(Text)
    questions = Column(Text)
    roles_required = Column(Text)
    channel_to_send = Column(Text)
    enabled = Column(Text)
    category = Column(Text)

class Application_Answers(Base):
    __tablename__ = "application_answers"

    app_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    user_id = Column(Text)
    app_name = Column(Text)
    q_a = Column(Text)
    verdict = Column(Text)
    reason = Column(Text)
    mod_id = Column(Text)
    channel_id = Column(Text)

class Level_Bonus_Roles(Base):
    __tablename__ = "level_bonus_roles"

    guild_id = Column(Text)
    role_id = Column(Text, primary_key=True)
    boost = Column(Text)

class Level_Bonus_Channels(Base):
    __tablename__ = "level_bonus_channels"

    guild_id = Column(Text)
    channel_id = Column(Text, primary_key=True)
    boost = Column(Text)

class Reminders(Base):
    __tablename__ = "reminders"

    reminder_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    channel_id = Column(Text)
    user_id = Column(Text)
    message = Column(Text)
    time = Column(Text)
    completed = Column(Text)

class UserStatistics(Base):
    __tablename__ = "user_statistics"

    unique_id = Column(Text, primary_key=True)
    guild_id = Column(Text)
    user_id = Column(Text)
    total_msgs = Column(Text)
    last_daily_msgs = Column(Text)
    last_weekly_msgs = Column(Text)
    last_monthly_msgs = Column(Text)

class GiveawayTempBoosters(Base):
    __tablename__ = "giveaway_temp_boosters"

    unique_id = Column(Text, primary_key=True)
    message_id = Column(Text)
    boost_role_id = Column(Text)
    boost_amount = Column(Text)

class ReportInfo(Base):
    __tablename__ = "report_info"

    guild_id = Column(Text)
    message_id = Column(Text, primary_key=True)
    reporter_id = Column(Text)
    reported_id = Column(Text)
    verdict = Column(Text)
    verdict_id = Column(Text)
    verdict_message = Column(Text)

class ReportMain(Base):
    __tablename__ = "report_main"

    guild_id = Column(Text, primary_key=True)
    channel_id = Column(Text)
    required_role = Column(Text)
    ping_role = Column(Text)
    mod_role = Column(Text)

class Autowelcomer(Base):
    __tablename__ = "autowelcomer"

    guild_id = Column(Text, primary_key=True)
    channel_id = Column(Text)
    image = Column(Boolean)
    welcome_message = Column(Text)
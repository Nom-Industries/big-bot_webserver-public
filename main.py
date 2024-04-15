from fastapi import FastAPI
from starlette.responses import RedirectResponse
from fastapi.openapi.docs import get_redoc_html
from fastapi import Depends
from fastapi.security.api_key import APIKey

from routers import guild_info, auto_threads, economy, private_voice_channels, sticky_messages, support, giveaway, suggestions, nickname, reaction_roles, autopublish, levels, notifications, applications, reminders, user_statistics

import uvicorn, constants, utils

app = FastAPI(openapi_url=None, title="Nom Industries API")

app.include_router(guild_info.guild_main_router)
app.include_router(guild_info.guild_mod_router)
app.include_router(guild_info.guild_logging_config_router)
app.include_router(guild_info.guild_stats_router)
app.include_router(auto_threads.router)
app.include_router(economy.router)
app.include_router(private_voice_channels.router)
app.include_router(sticky_messages.router)
app.include_router(support.router)
app.include_router(giveaway.router)
app.include_router(suggestions.router)
app.include_router(nickname.router)
app.include_router(reaction_roles.router)
app.include_router(autopublish.router)
app.include_router(levels.router)
app.include_router(notifications.router)
app.include_router(applications.router)
app.include_router(reminders.router)
app.include_router(user_statistics.router)

@app.get("/", include_in_schema=False)
def home():
    return "nom!"

@app.get("/json")
def json_api(api_key: str = None):
    if api_key != constants.DB_API_KEY:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    
    openapi = app.openapi()
    openapi["paths"].pop("/json")
    openapi["paths"].pop("/docs")
    openapi["paths"].pop("/redoc")

    return openapi

@app.get("/docs")
@app.get("/redoc")
def funny(api_key: APIKey = Depends(utils.validate_api_key)):
    return get_redoc_html(title="Big Bot", openapi_url="/json?api_key={API_KEY}")
        
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)

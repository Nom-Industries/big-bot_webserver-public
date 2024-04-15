from fastapi.security.api_key import APIKeyQuery

DBENDPOINT = ""
DBUSER = ""
DBPASS = ""
DBNAME = ""
DBPORT = 3306
DBURL = "mysql+pymysql://{DBUSER}:{DBPASS}{DBENDPOINT}/{DBUSER}"
DB_API_KEY = ""
API_KEY_QUERY = APIKeyQuery(name="api_key")
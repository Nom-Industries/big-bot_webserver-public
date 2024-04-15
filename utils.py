from constants import DB_API_KEY, API_KEY_QUERY

from fastapi import HTTPException, status, Security
from fastapi.responses import JSONResponse

def validate_api_key(api_key: str = Security(API_KEY_QUERY)):
    if api_key != DB_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )

def return_response(data):
    return data if data else JSONResponse({"error": "Not Found", "details": f"No data found"})

def check_if_exists(data, modifying = False):
    if data and not modifying:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The data sent to the database already exists"
        )
    
    elif not data and modifying:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="The data sent to the database does not exist"
        )

def validate_param(data_type: str, class_name: object):
    if data_type not in class_name.__dict__["__fields__"].keys():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid parameter value '{data_type}' for data_type param. Valid values for data_type parameter are: " + ', '.join(class_name.__dict__["__fields__"].keys())
        )

def convert_data_values(query, data_type):
    not_list = False
    if not isinstance(query, list):
        query = [query]
        not_list = True

    for i in range(len(query)):
        for j in data_type.__dict__["__fields__"].keys():
            if isinstance(query[i].__dict__[j], float):
                continue

            try:
               query[i].__dict__[j] = int(query[i].__dict__[j])
            
            except:
                pass

    return query if (isinstance(query, list) and not not_list) else query[0]
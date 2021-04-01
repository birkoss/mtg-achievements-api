# Endpoints

## POST /v1/login

Params : 

email - string
password - string

Return :

Status : 200 - OK
token - string
userId - string

Status : 404 Not Found
message - string
    - invalid_data : When a user is not found



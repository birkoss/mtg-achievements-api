# Install

## Must load initial data (data/player_role.json) *BEFORE* creating an admin

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
error - string
    - invalid_data : When a user is not found


## POST /v1/register

Params : 

email - string
password - string

Return :

Status : 200 - OK
token - string
userId - string

Status : 404 Not Found
error - string
    - blank : Missing username or password
    - unique : Email already exists


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

## GET /v1/playgroup/PLAYGROUP_ID/players

Return :

Status : 200 - OK
playgroupId - string
players - List of player (email and role)

## POST /v1/playgroup/PLAYGROUP_ID/players

Params :

email - string
role - string

Return :

Status : 200 - OK
playgroupId - string
players - List of player (email and role)

Status : 400
error - string
    - invalid_playgroup : Playgroup not valid of you don't have the permission to access it
    - missing_email_role : Params are missing in the query
    - invalid_email : email is not a valid email
    - invalid_role : role is not a valid existing role
    - already_in_playgroup : This user is already in this playgroup
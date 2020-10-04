import requests

NHL_STATS_API = 'https://statsapi.web.nhl.com/api/v1/'
TEAMS_API = NHL_STATS_API + 'teams/'

def query_teams():
    r = requests.get('TEAMS_API')
    return r.json()['teams']

def query_team_id(id):
    r = requests.get('TEAMS_API' + repr(id))
    return r.json()['teams'][0]
import requests

NHL_STATS_API = 'https://statsapi.web.nhl.com/api/v1/'
TEAMS_API = NHL_STATS_API + 'teams/'

def __build_team_query(id, roster=False, team_stats=False):
    q = _build_team_id_query(id)
    
    # All new optional arguments must be added to this list
    if(any((roster, team_stats))):
        q = q + '?'
    
    if(roster):
        q = q + 'expand=team.roster&'
    
    if(team_stats):
        q = q + 'expand=team.stats&'
        
    return q

# Builds the query which returns the team corresponding to ID
def _build_team_id_query(id):
    return TEAMS_API + repr(id)

# Returns all teams
def query_all_teams():
    r = requests.get(TEAMS_API)
    return r.json()['teams']

def query_team(id):
    q = __build_team_query(id, roster=True, team_stats=True)
    r = requests.get(q)
    return r.json()['teams'][0]

def query_roster(id):
    q = __build_team_query(id, roster=True)
    r = requests.get(q)
    return r.json()['teams'][0]['roster']['roster']

# def query_team_games(id):
    
import requests
from teams import Team

NHL_FRANCHISES_API = 'https://statsapi.web.nhl.com/api/v1/franchises'
NHL_TEAMS_API = 'https://statsapi.web.nhl.com/api/v1/teams'

def get_all_teams_data():
    r = requests.get(NHL_TEAMS_API)
    return r.json()['teams']

l = []
for team in get_all_teams_data():
    T = Team()
    T.id = team['id']
    T.name = team['name']
    T.division = team['division']
    T.conference = team['conference']
    l.append(T)

for t in l:
    print(t.name)
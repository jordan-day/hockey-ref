import pytest
from teams import Team

@pytest.fixture
def teamdata(monkeypatch):
    canucks_data = {'id': 23, 'name': 'Vancouver Canucks', 'link': '/api/v1/teams/23', 'venue': {'id': 5073, 'name': 'Rogers Arena', 'link': '/api/v1/venues/5073', 'city': 'Vancouver', 'timeZone': {'id': 'America/Vancouver', 'offset': -7, 'tz': 'PDT'}}, 'abbreviation': 'VAN', 'teamName': 'Canucks', 'locationName': 'Vancouver', 'firstYearOfPlay': '1970', 'division': {'id': 15, 'name': 'Pacific', 'nameShort': 'PAC', 'link': '/api/v1/divisions/15', 'abbreviation': 'P'}, 'conference': {'id': 5, 'name': 'Western', 'link': '/api/v1/conferences/5'}, 'franchise': {'franchiseId': 20, 'teamName': 'Canucks', 'link': '/api/v1/franchises/20'}, 'shortName': 'Vancouver', 'officialSiteUrl': 'http://www.canucks.com/', 'franchiseId': 20, 'active': True}
    monkeypatch.setattr(Team,"_find_id", lambda unused: 1)
    monkeypatch.setattr(Team,"_get_team_data", lambda unused: canucks_data)


def test_teamname():
    t = Team('Canucks')
    assert(t.name == 'Canucks')

def test_team_division():
    t = Team('Canucks')
    assert(type(t.division) is dict)
    assert(t.division)

def test_team_conference():
    t = Team('Canucks')
    assert(type(t.conference) is dict)
    assert(t.conference)

def test_teamname_notfound():
    with pytest.raises(ValueError) as excinfo:
        t = Team('abcde')
        assert(t is None)
    assert(excinfo is not None)

def test_find_teamid():
    t = Team('Canucks')
    assert(t is not None)
    assert(t._id is not None)
    
def test_get_roster():
    t = Team('Canucks')
    assert(type(t.players) is list)
    assert(t.players)
    
# def test_get_games():
#     t = Team('Canucks')
#     assert(t.games)
#     assert(type(t.games) is list)

def test_get_record():
    t = Team('Canucks')
    record = t.get_record()
    assert(record['wins'])
    assert(record['losses'])
    assert(record['OTL'])
    assert(record['wins'] + record['losses'] + record['OTL'] == record['games'])
    assert(2*record['wins'] + record['OTL'] == record['points'])
    
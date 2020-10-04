import query

class Team:
    """ A class containing various different information related to an NHL team """

    def __init__(self, name):
        if not self._name_exists(name):
            raise ValueError('An NHL team with that name doesn\'t exist')

        self.name = name    
        self._id = self._find_id()
        self._team_data = self._get_team_data()
        self.players = []
        self.division = self._team_data['division']
        self.conference = self._team_data['conference']
        self.games = []

    def _name_exists(self, name):
        for team in query.query_teams():
            if team['teamName'] == name:
                return True
        return False
    
    def _get_team_data(self):
        if self._id is None:
            raise ValueError("Team ID not set")
        return query.query_team_id(self._id)

    def _find_id(self):
        for team in query.query_teams():
            if team['teamName'] == self.name:
                return team['id']

    def get_roster(self):
        pass # return r.json()

    def pull_data(self):
        pass


    # ID
    # name
    # players
    # division
    # conference
    # games - list of games for current season
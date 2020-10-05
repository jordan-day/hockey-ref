import query

class Team:
    """ A class containing various different information related to an NHL team """

    def __init__(self, name):
        if not self._name_exists(name):
            raise ValueError('An NHL team with that name doesn\'t exist')

        self.name = name
        self._id = self._find_id()
        self.players = {}
        self.division = {}
        self.conference = {}
        self.team_stats = {}
        
        self._get_team_data()
        # self.games = []

    def _name_exists(self, name):
        for team in query.query_all_teams():
            if team['teamName'] == name:
                return True
        return False
    
    def _get_team_data(self):
        q = query.query_team(self._id)
        self.players = q['roster']['roster']
        self.division = q['division']
        self.conference = q['conference']
        self.team_stats = q['teamStats'][0]['splits'][0]['stat']

    def _find_id(self):
        for team in query.query_all_teams():
            if team['teamName'] == self.name:
                return team['id']

    # def _get_team_games(self):
    #     return query.query_team_games(self._id)

    def get_record(self):
        record = {}
        record['wins'] = self.team_stats['wins']
        record['losses'] = self.team_stats['losses']
        record['OTL'] = self.team_stats['ot']
        record['games'] = self.team_stats['gamesPlayed']
        record['points'] = self.team_stats['pts']
        return record
        
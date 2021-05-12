class Game():

    players = []
    opened = 0
    started = 0
    finished = None

    def __init__(self, game):
        self.players = game['players']
        self.team_one = ','.join([x['name'] for x in game['players'] if x['team'] == 1 and x['name'] != None])
        self.team_two = ','.join([x['name'] for x in game['players'] if x['team'] == 2 and x['name'] != None])
        self.team_ffa = ' vs '.join([x['name'] for x in game['players'] if x['team'] == -1 and x['name'] != None])

        self.opened = game['opened']
        self.started = game['started']
        self.finished = game['finished']
        self.num_players = game['num_players']

    def __str__(self):
        if len(self.team_ffa) > 3:
            return f"{self.team_ffa}"
        else:
            return f"{self.team_one}' vs {self.team_two}"

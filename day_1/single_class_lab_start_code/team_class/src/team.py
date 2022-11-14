class Team:

    

    def __init__(self, input_team_name, input_players, input_coach):
        self.name = input_team_name
        self.players = input_players
        self.coach = input_coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)
        
    def has_player(self, player):
        for element in self.players:
            if element == player:
                return True
        return False
    
    def play_game(self, result):
        if result == True:
            self.points += 3
            
        
        


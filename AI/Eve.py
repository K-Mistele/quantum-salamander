class Eve():

    behavior_string = "Very cooperative, and has faith in other people"
    gender = "female"

    def __init__(self, goes_first=True):
        self.score = 0
        self.goes_first = goes_first



    def first_turn(self):
        return "cooperate"

    def take_turn(self, data):
        #NOTE: data should be a list of past games, with own prev. choice first
        try:
            last_three_games = [data[-1], data[-2], data[-3]]
        except:
            try:
                last_three_games = [data[-1], data[-2]]
            except:
                last_three_games = [data[-1]]

        # behavior if the other AI is being very uncooperative
        if (["compete", "cooperate"] not in last_three_games or
            ["cooperate", "cooperate"] not in last_three_games):
            return "compete"
        else:
            return "cooperate"



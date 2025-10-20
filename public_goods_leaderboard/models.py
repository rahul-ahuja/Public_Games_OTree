from otree.api import *

doc = """
Repeated public goods game with stranger matching and leaderboard.
"""

class C(BaseConstants):
    NAME_IN_URL = 'public_goods'
    PLAYERS_PER_GROUP = 3
    NUM_ROUNDS = 5
    ENDOWMENT = 21 #please check this, you might be confusing number of total participants with endowment
    MULTIPLIER = 1.6

class Subsession(BaseSubsession):
    pass
    
def creating_session(subsession):
    #subsession.group_randomly() # Issue 3: here the players are randomly matched with each other in the group
    
    # Solution: Below implementation ensures that players matched in a predefined interaction of the players
    # I predefine the 3D matrix representing 21 people, 5 rounds, 3 players in a group ensuring that the players
    # don't rematched into a group if they have already been in previous rounds. 
    # Player IDs are assigned based on the following given in https://otree.readthedocs.io/en/latest/models.html
    # Player id_in_group: Automatically assigned integer starting from 1. In multiplayer games, 
    # indicates whether this is player 1, player 2, etc. This helps to assign values of the players in the predefined group matrix
    # This means that the first player will be assigned ID of 1, second player will be with ID of 2 and so on.

    group_matrix = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20, 21]],
    [[1, 4, 7], [2, 5, 8], [3, 6, 9], [10, 13, 16], [11, 14, 19], [12, 17, 20], [15, 18, 21]],
    [[1, 5, 9], [2, 4, 10], [3, 7, 11], [6, 8, 12], [13, 17, 21], [14, 18, 20], [15, 16, 19]],
    [[1, 6, 10], [2, 7, 12], [3, 4, 8], [5, 11, 17], [9, 15, 20], [13, 18, 19], [14, 16, 21]],
    [[1, 8, 13], [2, 6, 14], [3, 5, 15], [4, 11, 18], [7, 16, 20], [9, 12, 21], [10, 17, 19]],
    ]
    subsession.set_group_matrix(group_matrix[subsession.round_number - 1]) # pass the matrix into the subsession
    #print(subsession.get_group_matrix())



class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

def set_payoffs(group):
    players = group.get_players()
    group.total_contribution = sum([p.contribution for p in players])
    group.individual_share = (group.total_contribution * C.MULTIPLIER) / C.PLAYERS_PER_GROUP
    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share

class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=C.ENDOWMENT)

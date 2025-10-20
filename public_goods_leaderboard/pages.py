from otree.api import *
from .models import C, Subsession, Group, Player

class Introduction(Page):
    def is_displayed(player):
        return player.round_number == 1

class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    def vars_for_template(player):
        return {
            'total_contribution': player.group.total_contribution,
            'individual_share': player.group.individual_share,
            'payoff': player.payoff,
        }


class Leaderboard(Page):
    def vars_for_template(player):
        all_players = player.subsession.get_players()
        leaderboard_data = []
        for p in all_players:
            leaderboard_data.append({
                'player_id': p.id_in_subsession,
                'is_own_group': p.group.id_in_subsession == player.group.id_in_subsession,
                'is_self': p == player,
                'contribution': p.field_maybe_none('contribution'),
            })

        #return {'leaderboard': leaderboard_data} # Issue 1: We need to sort the leaderboard data 

        # Solution: sorted built-in function is used on the leaderboard which is a list of dictionaries. 
        # The dictionary has key-value pairs. One of the key-value pair is "contribtion" : value of the contribution
        # leaderboard list is being sorted in reverse order based on the key which is passed with lambda function which returns value of contribution
        # If the contribution value is None then it is return as negtive inifinity because sorting works on the numerical data types. 
        
        sorted_leaderboard_data = sorted(leaderboard_data, 
                                         key= lambda x: x['contribution'] if x['contribution'] is not None else -float('inf'), 
                                         reverse=True)
        
        return {'leaderboard': sorted_leaderboard_data}


page_sequence = [Introduction, Contribution, ResultsWaitPage, Results, Leaderboard]

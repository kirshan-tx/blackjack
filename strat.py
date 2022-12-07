
def strat(player_score: list[int], dealer_score: list[int]) -> str:
    """
    Takes in the player and dealer scores and return the strategy 

    :param player_score: Player score
    :param dealer_score: Dealer score
    :return: None
    """

    H = 'Hit!'
    S = 'Stand.'

    player = sum(player_score)
    dealer = int(dealer_score[0])

    #soft totals
    if 11 in player_score:
        other = player - 11 #other card that is not the ace

        if other >= 8:
            return S
        
        if other == 7 and dealer in range(2,9):
            return S
        
        if other == 7 and dealer in range(9,12):
            return H

        # <6
        return H

    #hard totals
    else:
        if player >= 17:
            return S
        if player in range(13,17) and dealer in range(7,12):
            return H 
        
        if player in range(13,17) and dealer in range(2,7):
            return S

        if player == 12 and dealer in range(4,7):
            return S
        
        if player == 12 and (dealer in range(2,4) or dealer in range(7,12)):
            return H
        
        # <11
        return H 
    
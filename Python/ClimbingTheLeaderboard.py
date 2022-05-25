#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    ranks = [1]
    count = 1
    for i in range(1, len(ranked)):
        if ranked[i] != ranked[i - 1]:
            count += 1
        ranks.append(count)
    ranked_position = -1
    player_rank = []
    for score in player:
        while ranked_position >= -len(ranks) and ranked[ranked_position] < score:
            ranked_position -= 1

        if ranked_position < -len(ranks):
            player_rank.append(1)
        elif ranked[ranked_position] == score:
            player_rank.append(ranks[ranked_position])
        else:
            player_rank.append(ranks[ranked_position] + 1)
    return player_rank

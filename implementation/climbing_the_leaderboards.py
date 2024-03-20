#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    score_set = sorted(set(ranked), reverse=True)
    player_score = []
    last_rank = 0
    for pl_score in reversed(player):
        player_rank = last_rank
        for rk_idx in range(last_rank, len(score_set)):
            if pl_score >= score_set[rk_idx]:
                player_score.append(player_rank+1)
                break
            elif rk_idx == len(score_set)-1 and pl_score < score_set[rk_idx]:
                player_score.append(player_rank+2)
                break
            player_rank += 1
            last_rank += 1
    return player_score[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
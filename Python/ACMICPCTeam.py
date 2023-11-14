#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    max_topics = 0
    teams_count = 0
    for i in range(len(topic)):
        t1 = topic[i]
        for j in range(i + 1, len(topic)):
            t2 = topic[j]
            count = compare_teams(t1, t2)
            if max_topics == count:
                teams_count += 1
            elif max_topics < count:
                max_topics = count
                teams_count = 1
    return [max_topics, teams_count]

def compare_teams(team1, team2):
    count = 0
    for i in range(len(team1)):
        if team1[i] == '1' or team2[i] == '1':
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

def luckBalance(k, contests):
    all_luck = [arr[0] for arr in contests]
    importance_ratings = [arr[1] for arr in contests]

    important_contest_luck = [all_luck[i] for i in range(len(all_luck)) if importance_ratings[i] == 1]
    if len(important_contest_luck) < k:
        return sum(importance_ratings)

    not_important_contest_luck = [all_luck[i] for i in range(len(all_luck)) if importance_ratings[i] == 0]

    max_luck = sum(not_important_contest_luck)
    important_contest_luck.sort()
    max_luck += sum(important_contest_luck[len(important_contest_luck) - k:])
    max_luck -= sum(important_contest_luck[:len(important_contest_luck) - k])
    return max_luck

def minimum_bribes(q):
    revised_q = [i - 1 for i in q]
    total_bribes = 0
    for i in range(len(revised_q)):
        # Check if a person has bribed more than 2 people
        if revised_q[i] - i > 2:
            print("Too chaotic")
            return
        # Check how many times a given person WAS BRIBED
        # Not checking how many times a person bribed someone else
        for j in range(max(0, revised_q[i] - 1), i):
            if q[j] > q[i]:
                total_bribes += 1
    print(total_bribes)

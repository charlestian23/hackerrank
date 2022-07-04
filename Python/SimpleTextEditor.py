if __name__ == "__main__":
    previous_states = ['']
    undo_location = [0]
    s = ''
    q = int(input())
    for i in range(q):
        operation = input().split()
        type = int(operation[0])
        if type == 1:
            s += operation[1]
            undo_location.append(len(previous_states) - 1)
        elif type == 2:
            k = int(operation[1])
            s = s[:len(s) - k]
            undo_location.append(len(previous_states) - 1)
        elif type == 3:
            k = int(operation[1])
            print(s[k - 1])
        else:
            if len(undo_location) == 0:
                continue
            index = undo_location.pop(-1)
            s = previous_states[index]
        previous_states.append(s)

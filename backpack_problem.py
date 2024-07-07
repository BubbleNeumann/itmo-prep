WEIGHTS = [3, 4, 5, 8, 9]
VALUES = [1, 6, 4, 7, 6]
MAX_WEIGHT = 13


def get_state_weight(state: int) -> int:
    weight = 0
    for i in range(len(WEIGHTS)):
        if state & (1 << i):
            weight += WEIGHTS[i]
    return weight


def get_state_val(state: int) -> int:
    val = 0
    for i in range(len(WEIGHTS)):
        if state & (1 << i):
            val += VALUES[i]
    return val


def bruteforce():
    """
    Bruteforce soulution. Complexity O(2^n)
    """
    max_val = 0
    max_state = None
    STATE_CNT = 2**len(WEIGHTS)

    for state in range(STATE_CNT):
        weight = get_state_weight(state)
        val = get_state_val(state)
        if weight <= MAX_WEIGHT:
            if val > max_val:
                max_val = val
                max_state = state

    print(max_val)
    print(bin(max_state))


def greedy():
    indices = [i for i in range(len(WEIGHTS))]
    res = []
    res_weight = 0
    res_val = 0

    while indices:
        max_val = 0
        max_index = 0
        for i in indices:
            if VALUES[i] > max_val:
                max_val = VALUES[i]
                max_index = i

        res_weight += WEIGHTS[max_index]

        if res_weight > MAX_WEIGHT:
            break

        res_val += VALUES[max_index]
        res.append(max_index)
        indices.remove(max_index)

    print(res_val)
    print(res)


if __name__ == "__main__":
    bruteforce()
    greedy()

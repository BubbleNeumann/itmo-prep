

weights = [3, 4, 5, 8, 9]
values = [1, 6, 4, 7, 6]
max_weight = 13

state_cnt = 2**len(weights)


def get_state_weight(state: int) -> int:
    weight = 0
    for i in range(len(weights)):
        if state & (1 << i):
            weight += weights[i]
    return weight


def get_state_val(state: int) -> int:
    val = 0
    for i in range(len(weights)):
        if state & (1 << i):
            val += values[i]
    return val


def bruteforce():
    """
    Bruteforce soulution. Complexity O(2^n)
    """
    max_val = 0
    max_state = None

    for state in range(state_cnt):
        weight = get_state_weight(state)
        val = get_state_val(state)
        if weight <= max_weight:
            if val > max_val:
                max_val = val
                max_state = state

    print(max_val)
    print(bin(max_state))


def greedy():
    indices = [i for i in range(len(weights))]
    res = []
    res_weight = 0
    res_val = 0

    while indices:
        max_val = 0
        max_index = 0
        for i in indices:
            if values[i] > max_val:
                max_val = values[i]
                max_index = i

        res_weight += weights[max_index]

        if res_weight > max_weight:
            break

        res_val += values[max_index]
        res.append(max_index)
        indices.remove(max_index)

    print(res_val)
    print(res)


if __name__ == "__main__":
    bruteforce()
    greedy()

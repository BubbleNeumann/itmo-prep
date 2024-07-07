

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


# bruteforce solution

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

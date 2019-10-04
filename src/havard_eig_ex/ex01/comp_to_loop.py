def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def comp_to_py(n):
    numbers = []
    for j in range(1,n,3):
        numbers.append(j**2)
    return numbers

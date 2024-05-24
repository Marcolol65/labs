def find_loser(n, m):
    current_cubes = m
    current_child = 1

    while True:
        cubes_to_take = min(current_child, current_cubes)

        if cubes_to_take > 25:
            cubes_to_take = 25

        current_cubes -= cubes_to_take

        if current_cubes == 0:
            return current_child

        current_child *= 2
        if current_child > n:
            current_child = 1


n = 5
m = 50
loser = find_loser(n, m)
print("The loser is child", loser)
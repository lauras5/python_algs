def longest_path_helper(x, y, torus, curr_path):
    if (x, y) in curr_path:
        return curr_path[(x, y)]

    longest = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for dx, dy in directions:
        nx, ny = (x + dx) % m, (y + dy) % n
        if 0 <= x < m and 0 <= y < n and torus[nx][ny] > torus[x][y]:
            path = longest_path_helper(nx, ny, torus, curr_path)
            if len(path) > len(longest):
                longest = path

    curr_path[(x, y)] = [(x, y)] + longest
    return curr_path[(x, y)]


# Define the main function to find the longest path in the torus
def longest_path(torus):
    if not torus or not torus[0]:
        return []

    # making global to access from helper function
    global m, n
    m, n = len(torus), len(torus[0])

    longest = []
    path_found = False

    for x in range(m):
        for y in range(n):
            path = longest_path_helper(x, y, torus, {})
            if len(path) > len(longest):
                longest = path
                path_found = True

    if path_found:
        return longest
    else:
        return []

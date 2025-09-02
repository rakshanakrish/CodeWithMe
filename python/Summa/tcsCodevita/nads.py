def solve():
    S = int(input())
    grid = [input() for _ in range(S)]

    overlaps = 0
    top_seen = set()

    for i in range(1, S-1):          # avoid borders
        for j in range(1, S-1):
            if grid[i][j] in "12":
                top = grid[i][j]
                # Check vertical & horizontal neighbors
                up, down = grid[i-1][j], grid[i+1][j]
                left, right = grid[i][j-1], grid[i][j+1]

                if (("1" in (up, down) and "2" in (left, right)) or
                    ("2" in (up, down) and "1" in (left, right))):
                    overlaps += 1
                    top_seen.add(top)

    if len(top_seen) == 2:
        print("Impossible")
    else:
        print(overlaps)

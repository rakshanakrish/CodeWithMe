from collections import deque

def can_place(grid, cells):
    M, N = len(grid), len(grid[0])
    for r, c in cells:
        if r < 0 or r >= M or c < 0 or c >= N or grid[r][c] == 'H':
            return False
    return True

def occupied(r, c, ori):
    # ori=0 -> horizontal, ori=1 -> vertical
    return [(r, c), (r, c+1)] if ori == 0 else [(r, c), (r+1, c)]

def neighbors(r, c, ori, grid):
    moves = []
    # move up/down/left/right
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if can_place(grid, occupied(nr, nc, ori)):
            moves.append((nr, nc, ori))
    # rotation check in 2x2 area
    if ori == 0:  # horizontal -> try vertical
        block = [(r,c),(r,c+1),(r+1,c),(r+1,c+1)]
        if can_place(grid, block):
            moves.append((r, c, 1))
            moves.append((r, c+1, 1))
    else:  # vertical -> try horizontal
        block = [(r,c),(r+1,c),(r,c+1),(r+1,c+1)]
        if can_place(grid, block):
            moves.append((r, c, 0))
            moves.append((r+1, c, 0))
    return moves

def find_positions(grid):
    sofa, target = [], []
    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 's':
                sofa.append((r,c))
            elif val == 'S':
                target.append((r,c))
    return sofa, target

def get_head_orientation(pos):
    (r1,c1),(r2,c2)=pos
    if r1==r2:  # horizontal
        return r1, min(c1,c2), 0
    else:       # vertical
        return min(r1,r2), c1, 1

def reached(r,c,ori,target_set):
    return set(occupied(r,c,ori)) == target_set

def sofa_problem():
    M, N = map(int, input().split())
    grid = [input().split() for _ in range(M)]

    sofa, target = find_positions(grid)
    if len(sofa) != 2 or len(target) != 2:
        print("Impossible", end="")
        return

    sr, sc, so = get_head_orientation(sofa)
    target_set = set(target)

    q = deque([(sr, sc, so, 0)])
    vis = {(sr, sc, so)}

    while q:
        r, c, ori, d = q.popleft()
        if reached(r, c, ori, target_set):
            print(d, end="")
            return
        for nr, nc, nori in neighbors(r, c, ori, grid):
            if (nr, nc, nori) not in vis:
                vis.add((nr, nc, nori))
                q.append((nr, nc, nori, d+1))
    print("Impossible", end="")

if __name__ == "__main__":
    sofa_problem()

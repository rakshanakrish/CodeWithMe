def safe_line():
    line = ""
    while line.strip() == "":
        line = input()
    return line.strip()
def safe_int():
    return int(safe_line())
def safe_int_list():
    return list(map(int, safe_line().split()))
def normalize360(a):
    return a % 360
def clock_angle_cost(time_str, Q, A, B, X, Y, queries):
    h, m = map(int, time_str.split(":"))
    hour_angle = normalize360((h % 12) * 30)
    minute_angle = normalize360(m * 6)
    total_cost = 0
    for T in queries:
        raw_diff = abs((hour_angle - minute_angle) % 360)
        diff = min(raw_diff, 360 - raw_diff)
        if diff == T:
            continue
        d0 = normalize360(hour_angle - minute_angle)
        desired_vals = {normalize360(T), normalize360(360 - T)}
        best_cost = float('inf')
        best_move = None
        for desired in desired_vals:
            s1 = (d0 - desired) % 360  
            cost_cw = s1 * Y * A
            cost_acw = (360 - s1) * Y * B
            if cost_cw <= cost_acw:
                if cost_cw < best_cost:
                    best_cost = cost_cw
                    best_move = ("min_only", s1)  
            else:
                if cost_acw < best_cost:
                    best_cost = cost_acw
                    best_move = ("min_only", s1 - 360)  
        for desired in desired_vals:
            required_total = (desired - d0) % 360  
            for hsign in (+1, -1):
                for steps in range(0, 13):
                    hmove = steps * 30
                    if hsign == 1:
                        mdeg = (required_total - hmove) % 360
                        hour_cost = hmove * X * A
                        minute_cost = mdeg * Y * B
                    else:
                        mdeg = ((-required_total) - hmove) % 360
                        hour_cost = hmove * X * B
                        minute_cost = mdeg * Y * A
                    cost = hour_cost + minute_cost
                    if cost < best_cost:
                        best_cost = cost
                        best_move = ("both", hsign, hmove, mdeg)
        if best_move is None:
            continue
        total_cost += best_cost
        if best_move[0] == "min_only":
            s_signed = best_move[1]
            minute_angle = normalize360(minute_angle + s_signed)
        else:
            _, hsign, hmove, mdeg = best_move
            hour_angle = normalize360(hour_angle + hsign * hmove)
            minute_angle = normalize360(minute_angle - hsign * mdeg)  
    return int(total_cost)
time_str = safe_line()
Q = safe_int()
A, B, X, Y = safe_int_list()
queries = [safe_int() for _ in range(Q)]
print(clock_angle_cost(time_str, Q, A, B, X, Y, queries))
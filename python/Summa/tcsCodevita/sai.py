def sai_mini_project():
    while True:
        line = input().strip()
        if line:
            balance = int(line)
            break
    while True:
        line = input().strip()
        if line:
            n = int(line)
            break
    transactions = []  
    commits = []    
    outputs = []      
    for _ in range(n):
        line = ""
        while not line:
            line = input().strip()
        parts = line.split()
        op = parts[0]
        if op == "read":
            outputs.append(balance)
        elif op == "credit":
            amt = int(parts[1])
            balance += amt
            transactions.append(("credit", amt, False))
        elif op == "debit":
            amt = int(parts[1])
            balance -= amt
            transactions.append(("debit", amt, False))
        elif op == "abort":
            idx = int(parts[1]) - 1
            if 0 <= idx < len(transactions) and not transactions[idx][2]:
                t_type, amt, _ = transactions[idx]
                if t_type == "credit":
                    balance -= amt
                else:  
                    balance += amt
                transactions[idx] = (t_type, amt, True)
        elif op == "rollback":
            commit_idx = int(parts[1]) - 1
            if 0 <= commit_idx < len(commits):
                balance = commits[commit_idx]
                transactions = []
                commits = commits[:commit_idx+1]
        elif op == "commit":
            commits.append(balance)
            transactions = [(t, a, True) for (t, a, _) in transactions]
    for val in outputs:
        print(val)
if __name__ == "__main__":
    sai_mini_project()
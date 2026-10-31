import json

def attacks(i, j, k, l):
    return k==l or abs(i - j) == abs(k - l)

def generate_n_queens(n):
    """
    Generate a list of clauses representing the n-queens problem for a given n.
    Each clause is represented as a list of literals, where each literal is a string.
    """
    clauses = {"kb": [], "goal": []}

    # 1. Qi = r The queen in column i is in row r
    cols = range(1, n + 1)
    
    kb = [
        [[f"Q{i}{j}", f"R{k}", f"R{l}"]]
        for i in cols
        for j in cols
        for k in cols
        for l in cols
        if i < j and not attacks(i, j, k, l)
    ]
    clauses["kb"].extend(kb)

    goal = [[f"Q{i}{j}", f"?q{i}", f"?q{j}"] for i in cols for j in cols if i < j]
    clauses["goal"].extend(goal)

    print(f"Generated {len(clauses["kb"])} clauses for the {n}-queens problem.")
    print(f"Generated {len(clauses["goal"])} goal clauses for the {n}-queens problem.")
    # print(clauses)
    return clauses

def save_json(clauses):
    """
    Save the given data to a JSON file.
    """
    with open(f"./fol_kbs/nQueens.json", "w") as f:
        lines = ['{', '    "kb" : [']
        for index, clause in enumerate(clauses["kb"]):
            comma = "," if index < len(clauses["kb"]) - 1 else ""
            lines.append(f"        {json.dumps(clause)}{comma}")

        lines.extend(['    ],', '', '    "goal" : ['])
        for index, clause in enumerate(clauses["goal"]):
            comma = "," if index < len(clauses["goal"]) - 1 else ""
            lines.append(f"        {json.dumps(clause)}{comma}")

        lines.extend(['    ]', '}'])
        f.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    n = 4  # Change this value to generate clauses for different sizes of the n-queens problem
    clauses = generate_n_queens(n)
    save_json(clauses)
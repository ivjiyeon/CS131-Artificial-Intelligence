from FOLClauses import FOLAtom, FOLClause, ResolveNodeFOL
from PropClauses import PropClause, ResolveNodeProp
import json
from pprint import pprint

def load_fol_kb(filepath: str) -> list:
    with open(filepath, "r") as f:
        data = json.load(f)

    kb = [
        FOLClause(*[FOLAtom(*atom) for atom in clause]) for clause in data["kb"]
    ]

    goal = FOLClause(*[FOLAtom(*atom) for atom in data['goal']])

    return kb, goal

def load_prop_kb(filepath: str) -> list:
    with open(filepath, "r") as f:
        data = json.load(f)

    kb = [
        PropClause(*clause) for clause in data["kb"]
    ]

    goal = PropClause(*data['goal'])

    return kb, goal

# Use set of support strategy to find try and locate the empty clause
class ResolutionProver:
    def __init__(self, kb=[], max_explore = 500):
        self.kb = kb
        self.max_explore = max_explore

    def prove(self, goal):
        solutions = []
        completed = True

        # 1.3/2.5: Resolution Prover
        ## BEGIN SOLUTION
        pending = [goal]
        next_node = 0

        # Explore breadth-first so recursive clauses cannot starve alternatives.
        while next_node < len(pending):
            current = pending[next_node]
            next_node += 1

            self.max_explore -= 1
            if self.max_explore <= 0:
                completed = False
                break

            if current.support.is_empty():
                solutions.append(current)
            else:
                pending.extend(current.generate_successors(self.kb))
            
        ## END SOLUTION
        return solutions, completed
    

def prove_propositional_statement(filename):
    kb, to_prove = load_prop_kb(filename)
    print("Propositional Knowledge Base:")
    pprint(kb)

    print("Statement to Prove:")
    pprint(to_prove)

    prover = ResolutionProver(kb)
    goal_clause = ResolveNodeProp(to_prove)

    proof, terminate = prover.prove(goal_clause)
    print("Terminated? ", terminate)

    if proof:
        print("Solution found!")
    else:
        print("No solutions found...")

def prove_fol_statement(filename):
    kb, to_prove = load_fol_kb(filename)
    pprint(kb)
    pprint(to_prove)

    prover = ResolutionProver(kb, max_explore=500)
    goal_clause = ResolveNodeFOL(to_prove)

    proof, terminate = prover.prove(goal_clause)
    print("Terminated? ", terminate)

    if proof:
        print("Solutions: ")
        for solution_node in proof:
            final_bindings = to_prove.get_final_bindings(solution_node.bindings)
            print(final_bindings)
    else:
        print("No solutions found...")


def main():
    print("Proving Propositional Statement: ")
    prove_propositional_statement("./prop_kbs/prop_kb_1.json")

    print()

    print("Proving FOL statement:")
    prove_fol_statement("./fol_kbs/nQueens.json")
    

if __name__ == "__main__":
    main()
class PropClause:
    def __init__(self, *literals):
        self.literals = list(literals)

    def is_empty(self):
        return len(self.literals) == 0

    def __str__(self):
        return "PropClause: "+str(self.literals)

    def __repr__(self):
        return "PropClause: "+str(self.literals)

    # Resolve a support clause against a kb_clause
    def support_resolve(support_clause, kb_clause):
        new_clause = None

        # 1.1: Propositional Support Resolve
        # BEGIN SOLUTION
        # only resolve if the first literal of kb_clause is the negation of the first literal of support_clause
        if kb_clause is not None and kb_clause.literals[0] == support_clause.literals[0]:
            new_literals = kb_clause.literals[1:]
            new_literals += support_clause.literals[1:] 
            new_clause = PropClause(*new_literals)
        # END SOLUTION

        return new_clause
        
class ResolveNodeProp:
    def __init__(self, support):
        self.support = support

    def __str__(self):
        return str(self.support)
    
    def __repr__(self):
        return "Resolution Prop Node: "+str(self.support)

    # Generate successors of a FOL node using the resolve function
    def generate_successors(self,kb):
        successors = []

        # 1.2: Generate Propositional Successors
        # BEGIN SOLUTION
        # add a new node for each clause in the KB that can be resolved with the support clause
        for knowledge in kb:
            new_clause = PropClause.support_resolve(self.support, knowledge)
            if new_clause is not None:
                successors.append(ResolveNodeProp(new_clause))

        # END SOLUTION

        return successors
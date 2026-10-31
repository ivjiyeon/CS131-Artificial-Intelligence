import uuid
class FOLAtom:
    def __init__(self, predicate, *args):
        self.atom = [predicate]+list(args) 

    def __repr__(self):
        return str(self.atom)
    
    def __str__(self):
        return str(self.atom)
    
    # Unify two FOLAtoms x and y with existing bindings
    def unify(x, y, bindings = {}):
        new_bindings = None

        # 2.1: Unify
        # BEGIN SOLUTION
        # identical atoms return the current bindings
        if x == y:
            return bindings
        # if x is a variable, check x or y already bound, if so unify with its binding, otherwise bind it to y
        elif isinstance(x, str) and x.startswith('?'):
            if x in bindings:
                return FOLAtom.unify(bindings[x], y, bindings)
            elif y in bindings:
                return FOLAtom.unify(x, bindings[y], bindings)
            else:
                new_bindings = bindings.copy()
                new_bindings[x] = y
                return new_bindings
        # if y is a variable, check x or y already bound, if so unify with its binding, otherwise bind it to x
        elif isinstance(y, str) and y.startswith('?'):
            if y in bindings:
                return FOLAtom.unify(x, bindings[y], bindings)
            elif x in bindings:
                return FOLAtom.unify(bindings[x], y, bindings)
            else:
                new_bindings = bindings.copy()
                new_bindings[y] = x
                return new_bindings
        # if both x and y are FOLAtoms, check if their predicates and arity match, then unify their arguments recursively
        elif isinstance(x, FOLAtom) and isinstance(y, FOLAtom):
            if x.atom[0] != y.atom[0] or len(x.atom) != len(y.atom):
                return False
            new_bindings = bindings.copy()
            for arg_x, arg_y in zip(x.atom[1:], y.atom[1:]):
                new_bindings = FOLAtom.unify(arg_x, arg_y, new_bindings)
                if new_bindings is False:
                    return False
        # if none of the above conditions are met, unification fails
        else:
            return False
        # END SOLUTION

        return new_bindings
    
    # Chase a binding through a bindings list
    def get_terminal_binding(var, intermediate_bindings):
        # 2.2: Get Terminal Bindings
        # BEGIN SOLUTION
        # If the variable is in the intermediate bindings, recursively chase its binding until a terminal value is found
        if var in intermediate_bindings:
            return FOLAtom.get_terminal_binding(intermediate_bindings[var], intermediate_bindings)
        
        # END SOLUTION

        return var

class FOLClause:
    def __init__(self, *atoms):
        self.atoms = list(atoms)

    def is_empty(self):
        return len(self.atoms) == 0


    def __str__(self):
        return "FOLClause: "+str(self.atoms)

    def __repr__(self):
        return "FOLClause: "+str(self.atoms)
    
    # Get the final bindings of a clause given a full binding list
    def get_final_bindings(self, intermediate_bindings):
        final_bindings = {}

        # 2.2: Chasing Bindings
        # BEGIN SOLUTION
        # iterate through each atom in the clause and for each variable in the atom, 
        # get its terminal binding using the intermediate bindings
        for atom in self.atoms:
            for var in atom.atom[1:]:
                if var.startswith('?'):
                    final_bindings[var] = FOLAtom.get_terminal_binding(var, intermediate_bindings)
        # END SOLUTION
        return final_bindings
    
    # Uniquify a clause with fresh variable names
    def uniquify(clause):
        unique_clause = []

        # 2.2: Uniquify
        # BEGIN SOLUTION
        variable_names = {}
        for atom in clause.atoms:
            unique_atom = [atom.atom[0]]
            for arg in atom.atom[1:]:
                if isinstance(arg, str) and arg.startswith('?'):
                    if arg not in variable_names:
                        variable_names[arg] = f"{arg}-{uuid.uuid4().hex}"
                    unique_atom.append(variable_names[arg])
                else:
                    unique_atom.append(arg)
            unique_clause.append(FOLAtom(*unique_atom))
        # END SOLUTION
        return unique_clause

    # Resolve a support clause against a kb_clause with existing bindings
    def support_resolve(support_clause, kb_clause, bindings={}):
        new_clause = None

        # 2.4: FOL Support Resolve
        # BEGIN SOLUTION
        if kb_clause is not None and len(kb_clause.atoms) > 0 and len(support_clause.atoms) > 0:
            unique_kb_atoms = FOLClause.uniquify(kb_clause)
            # Attempt to unify the first atom of the kb_clause with the first atom of the support_clause
            new_bindings = FOLAtom.unify(unique_kb_atoms[0], support_clause.atoms[0], bindings)
            if new_bindings is not False:
                # If unification is successful, create a new clause with the remaining atoms from both clauses
                new_atoms = unique_kb_atoms[1:] + support_clause.atoms[1:]
                new_clause = FOLClause(*new_atoms)
                return new_clause, new_bindings
            
        # END SOLUTION

        return new_clause
    

class ResolveNodeFOL:

    def __init__(self, support, bindings = {}):
        self.support = support
        self.bindings = bindings

    def __str__(self):
        return str(self.support)+" : "+str(self.bindings)
    
    def __repr__(self):
        return "Resolution FOL Node: "+str(self.support)+" : "+str(self.bindings)

    # Generate successors of a FOL node using the resolve function
    def generate_successors(self,kb):
        successors = [] 

        # 2.4: Generate FOL Successors
        # BEGIN SOLUTION
        for knowledge in kb:
            result = FOLClause.support_resolve(self.support, knowledge, self.bindings)
            if result is not None:
                new_clause, new_bindings = result
                successors.append(ResolveNodeFOL(new_clause, new_bindings))
        # END SOLUTION
                

        return successors

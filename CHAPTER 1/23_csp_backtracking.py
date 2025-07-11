def is_valid(assignment, var, value):
    for k in assignment:
        if assignment[k] == value:
            return False
    return True

def backtrack(variables, domain, assignment={}):
    if len(assignment) == len(variables):
        return assignment
    var = [v for v in variables if v not in assignment][0]
    for value in domain:
        if is_valid(assignment, var, value):
            assignment[var] = value
            result = backtrack(variables, domain, assignment)
            if result:
                return result
            del assignment[var]
    return None

print(backtrack(["X", "Y", "Z"], [1,2,3]))
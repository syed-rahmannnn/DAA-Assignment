rules = {
    "cold": ["wet"],
    "wet": ["rain"]
}
facts = {"rain"}

def backward(goal):
    if goal in facts:
        return True
    if goal in rules:
        return all(backward(subgoal) for subgoal in rules[goal])
    return False

print("Is cold?", backward("cold"))
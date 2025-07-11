percepts = {"breeze": True, "stench": False}

def wumpus_agent(percepts):
    if percepts["breeze"]:
        return "Caution: pit nearby"
    elif percepts["stench"]:
        return "Caution: wumpus nearby"
    return "Move forward"

print(wumpus_agent(percepts))
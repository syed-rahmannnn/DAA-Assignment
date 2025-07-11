class GoalAgent:
    def __init__(self, goal):
        self.goal = goal

    def decide(self, state):
        return "move" if state != self.goal else "stop"

g = GoalAgent("clean")
print(g.decide("dirty"))
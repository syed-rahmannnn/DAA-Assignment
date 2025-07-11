class LearningAgent:
    def __init__(self):
        self.knowledge = {}

    def learn(self, percept, action):
        self.knowledge[percept] = action

    def act(self, percept):
        return self.knowledge.get(percept, "explore")

agent = LearningAgent()
agent.learn("dirty", "clean")
print(agent.act("dirty"))
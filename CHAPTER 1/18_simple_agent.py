class Agent:
    def act(self, percept):
        if percept == "dirty":
            return "clean"
        else:
            return "move"

agent = Agent()
print(agent.act("dirty"))
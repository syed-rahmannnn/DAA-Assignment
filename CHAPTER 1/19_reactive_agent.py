class ReactiveAgent:
    def respond(self, percept):
        return "clean" if percept == "dirty" else "move"

r = ReactiveAgent()
print(r.respond("dirty"))
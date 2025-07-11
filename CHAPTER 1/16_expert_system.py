def expert_system(facts):
    if facts.get("hungry") and not facts.get("food"):
        return "Go shopping"
    return "Relax"

print(expert_system({"hungry": True, "food": False}))
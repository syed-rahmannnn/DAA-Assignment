facts = {"sunny": True, "have_umbrella": False}
rules = [("go_outside", lambda f: f["sunny"] and not f["have_umbrella"])]

for action, rule in rules:
    if rule(facts):
        print(f"You should: {action}")
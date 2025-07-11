facts = {"rain"}
rules = [("wet", {"rain"}), ("cold", {"wet"})]
known = set(facts)

while True:
    applied = False
    for conclusion, premises in rules:
        if premises.issubset(known) and conclusion not in known:
            known.add(conclusion)
            print("Inferred:", conclusion)
            applied = True
    if not applied:
        break
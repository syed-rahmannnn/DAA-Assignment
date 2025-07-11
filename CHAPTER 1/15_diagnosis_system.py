def diagnose(symptoms):
    if "fever" in symptoms and "cough" in symptoms:
        return "Flu"
    elif "headache" in symptoms:
        return "Migraine"
    return "Unknown"

print(diagnose(["fever", "cough"]))
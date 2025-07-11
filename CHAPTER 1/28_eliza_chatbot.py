def eliza(msg):
    if "mother" in msg:
        return "Tell me more about your mother."
    return "Why do you say that?"

print(eliza("I miss my mother"))
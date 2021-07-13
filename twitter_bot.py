import random

def memify(text):
    new = []
    for c in text:
        r = random.randint(0, 1)
        if r:
            new.append(c.upper()) 
        else:
            new.append(c.lower())
    return ''.join(new)


print(memify("hello my name is whasso i am a cool guy"))
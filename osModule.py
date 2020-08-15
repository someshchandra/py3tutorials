import os

result = []

def recurse(input):
    paths = os.listdir(input)
    for path in paths:
        formatted = input + os.sep + path
        if not os.path.isdir(formatted):
            result.append(formatted)
        else:
            recurse(formatted)

recurse(os.getcwd())
print(result)

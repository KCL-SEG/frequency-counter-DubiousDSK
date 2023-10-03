"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    newList = []
    # Your code goes here
    i = 0
    while i < len(items):
        if type(items[i]) == int:
            newList.append(str(items[i]))
        else:
            newList.append(items[i])
        i += 1

    for x in newList:
        counter = 0
        for y in newList:
            if x == y:
                counter += 1
        frequencies.update({x : counter})
    
    return frequencies
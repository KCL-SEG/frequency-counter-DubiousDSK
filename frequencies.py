"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    i = 0
    while i < len(items):
        if type(items[i]) == int:
            items.remove(items[i])
            items.append(str(items[i]))
        ++i
    
    for x in items:
        counter = 0
        for y in items:
            if x == y:
                items.remove[y]
                counter += 1
        frequencies[x] = counter
 
    return frequencies

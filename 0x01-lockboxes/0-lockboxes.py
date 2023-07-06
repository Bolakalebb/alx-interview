#!/usr/bin/python3
"""
a method that determines if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    keys = [0]  # Start with the keys in the first box

    while keys:
        current_box = keys.pop()

        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)

    return all(unlocked)

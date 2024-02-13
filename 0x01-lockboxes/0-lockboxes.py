#!/usr/bin/python3
'''
Module: lockbox_solver

This module provides a function for checking if all the lockboxes in a list
can be unlocked, given that the first box is unlocked.
'''


def canUnlockAll(boxes):
    '''
    Function: canUnlockAll

    Description:
    Checks if all the lockboxes in a list of boxes containing
    the keys (indices)
    to other boxes can be unlocked, assuming the first box is already unlocked.

    Parameters:
    - boxes (list): A list of lockboxes, where each box is represented as a
    list of indices to other boxes.

    Returns:
    - bool: True if all lockboxes can be unlocked, False otherwise.
    '''
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        boxIdx = unseen_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[boxIdx])
            seen_boxes.add(boxIdx)
    return n == len(seen_boxes)

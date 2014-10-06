from random import random

def _get_random_index(num):
    return int(random()*num)

def pick_one_random_item(lst):
    """
    Picks one random item from a list
    """
    assert isinstance(lst,list)
    size = len(lst)
    if size < 1:
        return None
    idx = _get_random_index(len(lst)-1)
    return lst[idx]

#Bogo sort Algorithm

import random
 
def bogosort(array):
    while not in_order(array):
        random.shuffle(array)
    return array
 
def in_order(array):
    if not array:
        return True
    last = array[0]
    for index in array[1:]:
        if index < last:
            return False
        last = index
    return True

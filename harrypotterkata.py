#!/usr/bin/env python3

import sys
import json
from typing import List
from collections import Counter

DISCOUNT_FACTORS = [1.0, 0.95, 0.9, 0.8, 0.75]

def get_lowest_price(combo: List[int]) -> float:
    if not combo:
        return 0.0
    counter = Counter(combo)
    occurrences = dict(counter)

    price = 0.0
    while occurrences:

        num_different_books = 0
        for k in list(occurrences.keys()):
            occurrences[k] -= 1
            num_different_books += 1
            if occurrences[k] <= 0:
                del occurrences[k]
        
        price += 8.0 * num_different_books * DISCOUNT_FACTORS[num_different_books - 1]

    return price

def main(argv):
    assert len(argv) > 2
    buys = json.loads(argv[1])
    print(get_lowest_price(buys))    

if __name__ == "__main__":
    main(sys.argv)
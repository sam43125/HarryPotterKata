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
    return 8.0 * len(counter.keys()) * DISCOUNT_FACTORS[len(counter.keys()) - 1]

def main(argv):
    assert len(argv) > 2
    buys = json.loads(argv[1])
    print(get_lowest_price(buys))    

if __name__ == "__main__":
    main(sys.argv)
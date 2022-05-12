#!/usr/bin/env python3

import sys
import json
from typing import List
from collections import Counter
from functools import lru_cache
import itertools

DISCOUNT_FACTORS = [1.0, 0.95, 0.9, 0.8, 0.75]

def get_lowest_price(combo: List[int]) -> float:

    @lru_cache(maxsize=None)
    def __get_lowest_price(*args) -> float:

        args = list(args)
        original_args = args[:]
        min_price = float('inf')
        for num_different_books in range(1, sum(v > 0 for v in original_args) + 1):
            price = 8.0 * num_different_books * DISCOUNT_FACTORS[num_different_books - 1]
            permutations = list(itertools.permutations(num_different_books * [1] + (5 - num_different_books) * [0]))
            for permutation in permutations:
                args = original_args[:]
                for book, number in enumerate(permutation):
                    if number:
                        if args[book] > 0:
                            args[book] -= 1
                        else:
                            break
                else:
                    price += __get_lowest_price(*sorted(args))
                    if price < min_price:
                        min_price = price
        
        return min_price if min_price != float('inf') else 0.0

    counter = Counter(combo)
    occurrences = dict(counter)
    args = [occurrences.get(book, 0) for book in range(5)]

    return __get_lowest_price(*args)

def main(argv):
    assert len(argv) >= 2
    buys = json.loads(argv[1])
    print(get_lowest_price(buys))    

if __name__ == "__main__":
    main(sys.argv)
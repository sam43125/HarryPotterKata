#!/usr/bin/env python3

import sys
import json
from typing import List

def get_lowest_price(combo: List[int]) -> float:
    return 0

def main(argv):
    assert len(argv) > 2
    buys = json.loads(argv[1])
    print(get_lowest_price(buys))    

if __name__ == "__main__":
    main(sys.argv)
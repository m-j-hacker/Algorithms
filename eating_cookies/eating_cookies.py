#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  total_cookies = n
  number_of_ways = 0
  if total_cookies < 0:
    return 'Ivalid input, number of cookies must be a positive integer!'

  if total_cookies == 0:
    return 
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')

    # Notes
    # The problem boils down to this - how many different times can
    # the given number be reduced by 1, 2, and 3?
    # 
    # Recursion holds the answer 
#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price_so_far = 0
  max_profit_so_far = 0
  # For this function, I'm going to run nested for loops that
  # will check the difference of n and n-1

  # My first attempt was not successful. I figured out that I was
  # over-complicating my loop - by running a single loop and checking
  # the minimum price against each number that came before it, we can
  # more effectively run the algorithm - Big O is O(n) for this function
  for i in range(len(prices)):
    if i == 0:
      current_min_price_so_far = prices[i]
      continue
    if prices[i] < current_min_price_so_far:
      current_min_price_so_far = prices[i]
      min_index = i

    if prices[i] > current_min_price_so_far and min_index < i:
      difference = prices[i] - current_min_price_so_far
      if difference > max_profit_so_far:
        max_profit_so_far = difference
  
  return max_profit_so_far



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
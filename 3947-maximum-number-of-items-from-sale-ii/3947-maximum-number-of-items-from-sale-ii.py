from typing import List
class Solution:
  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    n = len(items)
    freq = [0] * (n + 1)
    for factor, _ in items:
      freq[factor] += 1
    multiples = [0] * (n + 1)
    for f in range(1, n + 1):
      if freq[f]:
        total = -1
        for m in range(f, n + 1, f):
          total += freq[m]
        multiples[f] = total
    min_price = min(price for _, price in items)
    items_sorted = sorted(items, key=lambda x: x[1])
    total_copies = 0
    rem_budget = budget
    for factor, price in items_sorted:
      if price >= 2 * min_price:
        break
      cap = multiples[factor]
      if cap > 0:
        can_buy = min(cap, rem_budget // price)
        total_copies += can_buy * 2
        rem_budget -= can_buy * price
    total_copies += rem_budget // min_price
    return total_copies
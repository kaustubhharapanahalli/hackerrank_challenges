"""
Challenge:         collections counter
Link to Challenge: https://www.hackerrank.com/challenges/collections-counter/problem

Author:            Kaustubh M. Harapanahalli
"""

from collections import Counter

number_of_shoes = int(input())
shoe_sizes_available = map(int, input().split())
counts_of_size = Counter(shoe_sizes_available)

number_of_customer = int(input())
total_price = 0

for i in range(number_of_customer):
    customer_query_size, price_paid = map(int, input().split())

    if counts_of_size[customer_query_size] != 0:
        counts_of_size[customer_query_size] -= 1
        total_price += price_paid
        
print(total_price)


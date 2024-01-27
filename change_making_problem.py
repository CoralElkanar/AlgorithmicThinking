"""
- Greedy Algorithm -

Question:
Find the minimum number of coins from a set of denominations that add up to a given amount of money.

Example: 
set of available coins denominations:
1p, 2p, 5p, 10p, 20p, 50p, $1, $2 (dollar sign represents the Pounds here)

* what is the minimum number of coins you need to make - 24p?
-> 20p + 2p + 2p
meaning - 3 coins

* what is the minimum number of coins you need to make - $1.63?
-> $1 + 50p + 10p + 2p + 1p
meaning - 5 coins

notice - 100p = $1
"""

def make_change(target_amount):
    # target_amount can be represented as $1.63 or 63p.
    if target_amount[0] == '$':
        target_amount_int = int(float(target_amount[1:])*100)
    else:
        target_amount_int = int(target_amount[:-1])
    coins = (1,2,5,10,20,50,100,200)
    change = []
    for coin in coins[::-1]:
        while target_amount_int >= coin:
            target_amount_int -= coin
            change.append(coin)
    return len(change)


change = '$1.63'
number_of_coins = make_change(change)
print(f"number of coins for making change to {change} is {number_of_coins}")

change = '24p'
number_of_coins = make_change(change)
print(f"number of coins for making change to {change} is {number_of_coins}")

change = '$24.23'
number_of_coins = make_change(change)
print(f"number of coins for making change to {change} is {number_of_coins}")

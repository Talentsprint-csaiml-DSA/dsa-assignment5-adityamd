def soln(coins, target_amount, sm):
    if sm == target_amount:
        return 0
    mn = -1
    for i in coins:
        if sm + i <= target_amount:
            tmp = 1 + soln(coins, target_amount, sm + i)
            if tmp == 0:
                return -1
            if mn == -1 or mn > tmp:
                mn=tmp
    return mn
 
def min_coins(coins, target_amount):
    return soln(coins, target_amount, 0)

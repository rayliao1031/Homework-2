def get_amount_out(amount_in, reserve_in, reserve_out):
    # Uniswap V2 的費率是0.3%，所以費後金額是997份
    amount_in_with_fee = amount_in * 997
    numerator = amount_in_with_fee * reserve_out
    denominator = reserve_in * 1000 + amount_in_with_fee
    amount_out = numerator / denominator
    return amount_out

# 定義流動性池
liquidity = {
    ("tokenB", "tokenA"): (10, 17), # tokenB to tokenA 的流動性
    ("tokenA", "tokenD"): (15, 9),  # tokenA to tokenD 的流動性
    ("tokenD", "tokenB"): (6, 13),  # tokenD to tokenB 的流動性
}

# 初始代幣及數量
initial_amount = 5

# 交易路徑
path = [
    ("tokenB", "tokenA"),
    ("tokenA", "tokenD"),
    ("tokenD", "tokenB"),
]

# 按照路徑交易
amount = initial_amount
for (from_token, to_token) in path:
    reserve_in, reserve_out = liquidity[(from_token, to_token)]
    amount = get_amount_out(amount, reserve_in, reserve_out)

print(f"Final path: {'->'.join([p[0] for p in path])}->{path[-1][1]}, tokenB balance={amount}")

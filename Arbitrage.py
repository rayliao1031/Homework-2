from collections import deque

liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def get_amount_out(amount_in, reserve_in, reserve_out):
    amount_in_with_fee = amount_in * 997.0
    numerator = amount_in_with_fee * reserve_out
    denominator = reserve_in * 1000.0 + amount_in_with_fee
    return numerator / denominator

def find_arbitrage_path(liquidity):
    paths = deque([(["tokenB"], 5.0)])  # 初始化路徑和初始餘額

    while paths:
        path, balance = paths.popleft()
        last_token = path[-1]

        # 尋找所有可能的下一步
        for (tokenA, tokenB), (reserveA, reserveB) in liquidity.items():
            if tokenA == last_token or tokenB == last_token:
                next_token = tokenB if tokenA == last_token else tokenA
                if next_token in path and next_token != "tokenB":
                    continue  # 避免重複訪問非起始點的代幣

                new_balance = get_amount_out(balance, reserveA if tokenA == last_token else reserveB, reserveB if tokenA == last_token else reserveA)
                new_path = path + [next_token]

                # 如果回到了tokenB且餘額大於20，立即返回這條路徑
                if next_token == "tokenB" and len(new_path) > 3 and new_balance > 20.0:
                    return new_path, new_balance
                elif next_token != "tokenB":
                    paths.append((new_path, new_balance))

    return [], 0.0  # 如果找不到符合條件的路徑

path, balance = find_arbitrage_path(liquidity)
print(f"Path: {'->'.join(path)}, tokenB balance={balance}")

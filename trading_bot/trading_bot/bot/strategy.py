import numpy as np

def simple_moving_average(prices, period=5):
    if len(prices) < period:
        return None
    return np.mean(prices[-period:])


def generate_signal(prices):
    avg = simple_moving_average(prices)

    if avg is None:
        return "HOLD"

    current_price = prices[-1]

    if current_price < avg:
        return "BUY"
    elif current_price > avg:
        return "SELL"
    else:
        return "HOLD"
    



# 👇 THIS IS TEST CODE (ADD HERE)
if __name__ == "__main__":
    test_prices = [100, 102, 101, 103, 105]
    print(generate_signal(test_prices))
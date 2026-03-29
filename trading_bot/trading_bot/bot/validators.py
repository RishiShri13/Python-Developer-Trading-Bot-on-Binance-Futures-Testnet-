def validate_order(symbol, side, order_type, quantity, price=None):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_MARKET"]:
        raise ValueError("Invalid order type")

    if float(quantity) <= 0:
        raise ValueError("Quantity must be positive")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price required for LIMIT orders")
from bot.client import BinanceClient
from bot.orders import place_order
from bot.validators import validate_order
from bot.logging_config import setup_logger
from bot.strategy import generate_signal
from binance.client import Client

from colorama import Fore, Style
from tabulate import tabulate

from dotenv import load_dotenv
import os

load_dotenv()

last_order = None

class BinanceClient:
    def __init__(self, API_KEY, API_SECRET):
        self.client = Client (
            API_KEY, 
            API_SECRET,
            testnet=True
            )

    def get_client(self):
        return self.client

def print_menu():
    print(Fore.CYAN + "\n=== 🚀 TRADING BOT MENU ===" + Style.RESET_ALL)
    print("1. Place Order")
    print("2. View Last Order")
    print("3. Exit")

def get_price(self, symbol):
    ticker = self.client.futures_symbol_ticker(symbol=symbol)
    return float(ticker["price"])   # MUST be float

def get_order_input():
    print(Fore.YELLOW + "\nEnter Order Details:" + Style.RESET_ALL)

    symbol = input("Symbol (BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    order_type = input("Type (MARKET/LIMIT/STOP_MARKET): ").upper()
    quantity = float(input("Quantity: "))

    price = None
    if order_type in ["LIMIT", "STOP_MARKET"]:
        price = float(input("Price / Stop Price: "))

    return symbol, side, order_type, quantity, price


def print_order_result(order):
    if "error" in order:
        print(Fore.RED + f"\n❌ Error: {order['error']}" + Style.RESET_ALL)
        return

    table = [
        ["Order ID", order.get("orderId")],
        ["Symbol", order.get("symbol")],
        ["Status", order.get("status")],
        ["Side", order.get("side")],
        ["Type", order.get("type")],
        ["Executed Qty", order.get("executedQty")],
    ]

    print(Fore.GREEN + "\n✅ Order Placed Successfully!\n" + Style.RESET_ALL)
    print(tabulate(table, tablefmt="grid"))


def main():
    global last_order

    setup_logger()

    print(Fore.CYAN + "=== 🔐 LOGIN ===" + Style.RESET_ALL)
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    
    client = BinanceClient(API_KEY, API_SECRET).get_client()

    client = BinanceClient(API_KEY, API_SECRET).get_client()

    while True:
        print_menu()
        choice = input("\nChoose option: ")

        if choice == "1":
            try:
                symbol, side, order_type, quantity, price = get_order_input()

                validate_order(symbol, side, order_type, quantity, price)

                print(Fore.YELLOW + "\n⏳ Placing Order..." + Style.RESET_ALL)

                result = place_order(client, symbol, side, order_type, quantity, price)

                last_order = result
                print_order_result(result)

            except Exception as e:
                print(Fore.RED + f"\n⚠️ Error: {e}" + Style.RESET_ALL)

        elif choice == "2":
            if last_order:
                print_order_result(last_order)
            else:
                print(Fore.YELLOW + "\nNo orders yet." + Style.RESET_ALL)

        elif choice == "3":
            print(Fore.CYAN + "\n👋 Exiting... Bye!" + Style.RESET_ALL)
            break

        else:
            print(Fore.RED + "\nInvalid choice!" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
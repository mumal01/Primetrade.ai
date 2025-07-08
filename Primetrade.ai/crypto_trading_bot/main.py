# main.py

from config import API_KEY, API_SECRET
from bot import BasicBot
from binance.enums import *

def main():
    print("Welcome to Binance Futures Trading Bot")

    bot = BasicBot(API_KEY, API_SECRET)

    symbol = input("Enter trading symbol (e.g., BTCUSDT): ").upper()
    side_input = input("Buy or Sell? ").strip().upper()
    order_type_input = input("Order Type (MARKET / LIMIT): ").strip().upper()
    quantity = float(input("Enter quantity: "))

    if side_input not in ["BUY", "SELL"]:
        print("Invalid side")
        return
    if order_type_input not in ["MARKET", "LIMIT"]:
        print("Invalid order type")
        return

    price = None
    if order_type_input == "LIMIT":
        price = input("Enter limit price: ")

    side = SIDE_BUY if side_input == "BUY" else SIDE_SELL

    order = bot.place_order(symbol, side, order_type_input, quantity, price)

    if order:
        print("Order executed:")
        print(order)
    else:
        print("Order failed. Check logs for details.")

if __name__ == "__main__":
    main()

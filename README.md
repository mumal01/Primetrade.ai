# Binance Futures Order Bot

## 📌 Overview

This project is a **CLI-based trading bot** for the Binance USDT-M Futures Testnet. It allows users to place **Market** and **Limit** orders with optional support for **Advanced Order Types** such as **Stop-Limit**, **OCO**, **TWAP**, and **Grid Trading**.

It features:
- Input validation for symbol, quantity, and price
- Structured logging of all activities
- Modular and extensible architecture
- Developer-friendly CLI usage

---

## 🧾 Features

| Feature               | Description                                            |
|----------------------|--------------------------------------------------------|
| ✅ Market Orders      | Place instant buy/sell trades at market price         |
| ✅ Limit Orders       | Set specific buy/sell price with GTC enforcement      |
| ⚙️ Stop-Limit (Bonus) | Trigger a limit order once a stop price is hit        |
| ⚙️ OCO Orders         | One-Cancels-the-Other (take-profit and stop-loss)     |
| ⚙️ TWAP Strategy      | Time-Weighted Average Price execution for large orders|
| ⚙️ Grid Orders        | Buy low/sell high within a defined price range        |
| 🧪 Input Validation   | Validates symbol format, price ranges, and quantity   |
| 📄 Logging            | All actions recorded in `bot.log` for transparency    |

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/yourname-binance-bot.git
cd yourname-binance-bot

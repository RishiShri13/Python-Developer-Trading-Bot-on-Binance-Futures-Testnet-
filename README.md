# 🚀 Python Trading Bot for Binance Futures Testnet — Automated Strategies, Smart Order Execution & Modular CLI Design

A beginner-friendly *Python-based trading bot* that can place *Market, Limit, and Stop-Market orders* on Binance Futures Testnet using a clean CLI interface, logging system, and modular architecture.

---

# 📌 Features

✅ Place *Market Orders*
✅ Place *Limit Orders*
✅ Place *Stop-Market Orders (Bonus)*
✅ Supports *BUY & SELL*
✅ Interactive *CLI Menu System*
✅ *Auto Trading Bot* (Strategy-based)
✅ Input validation & error handling
✅ Logging of API requests and errors
✅ Clean and modular project structure
✅ Environment variable support (.env for API keys)

---

# 🧠 Tech Stack

* Python 3.x
* python-binance
* numpy
* colorama
* tabulate
* python-dotenv

---

# 📂 Project Structure


trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│   ├── strategy.py
│
├── cli.py
├── auto_bot.py
├── requirements.txt
├── README.md
├── .env


---

# ⚙️ Installation & Setup

## 1. Clone Repository


git clone <your-repo-link>
cd trading_bot


---

## 2. Install Dependencies


pip install -r requirements.txt


OR


pip install python-binance colorama tabulate numpy python-dotenv


---

## 3. Create .env File

Create a file named .env in the root folder:


API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret


---

# 🔑 Binance Testnet Setup

1. Go to: https://testnet.binancefuture.com
2. Login (GitHub login supported)
3. Go to *API Management*
4. Create API Key
5. Copy API Key & Secret
6. Paste into .env

⚠️ Use *Futures Testnet only*, not real Binance API.

---

# ▶️ How to Run

## Run CLI Bot


python cli.py


---

## Run Auto Trading Bot


python auto_bot.py


---

# 🖥️ CLI Menu


=== TRADING BOT MENU ===

1. Place Order
2. View Last Order
3. Exit


---

# 🧪 Example Input


Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001


---

# 📊 Output Example


✅ Order Placed Successfully!

+--------------+-----------+
| Order ID     | 12345678  |
| Symbol       | BTCUSDT   |
| Status       | FILLED    |
| Side         | BUY       |
+--------------+-----------+


---

# 🤖 Auto Trading Strategy

This bot includes a *Simple Moving Average Strategy*:

* If current price < average → BUY
* If current price > average → SELL
* Otherwise → HOLD

---

# 🧾 Logging

All logs are stored in:


bot.log


Includes:

* API requests
* Order responses
* Errors

---

# ⚠️ Important Notes

* This project uses *Binance Futures Testnet* (no real money)
* Do NOT use real API keys
* Always keep .env file private

---

# 🔐 Security

Add .env to .gitignore:


.env


---

# 🚀 Future Improvements

* RSI / MACD strategy
* Stop-loss & Take-profit
* GUI dashboard
* Telegram alerts
* AI-based trading

---

# 👨‍💻 Author

Rishi Shrivastava
B.Tech CSE 

---

# ⭐ Interview Highlight

> Built a modular CLI-based trading bot with Binance Futures API integration, automated strategy execution, and secure environment variable management.

---

# 📜 License

This project is for educational purposes only.

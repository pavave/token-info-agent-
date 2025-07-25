# 🤖 Token Info Agent

Telegram bot to fetch real-time token prices using CoinGecko and DexScreener APIs.

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/pavave/token-info-agent-.git
cd token-info-agent-
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv venv
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```powershell
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration

1. Create `.env` file:

```bash
nano .env
```

2. Edit `.env` and add your actual bot token:

```env
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_API_KEY
```

---

## 🚀 Running the Bot

```bash
python main.py
```

---

## 💬 Usage

Open Telegram, find your bot by username, start chatting, and try queries like:

- What's the price of ETH?
- Price of SOL?
- How much is PEPE?

The bot will reply with live token price info from CoinGecko or DexScreener.

---

## 📁 Project Structure

```
token-info-agent/
├── main.py              # Telegram bot logic
├── token_utils.py       # Price fetching logic
├── requirements.txt     # Dependencies
├── .env.example         # Env config example
├── README.md            # This file
└── prompt_examples.txt  # Sample prompts
```

---

## 🎥 Demo Video

_(Coming soon: link to YouTube demo)_

---

## 🛠 Tech Stack

- Python 3.8+
- `python-telegram-bot`
- CoinGecko API
- DexScreener API
- `requests`, `dotenv`

---

## 🧠 Future Ideas

- Currency conversion (e.g., ETH → EUR)
- Batch queries
- Price alerts
- Web/CLI interface
- LLM integration for better NLP

---

## 📜 License

MIT — free to use, modify, distribute.

---

## 🤝 About

Created as part of the **Shade Agents** initiative on the NEAR blockchain ecosystem, showcasing autonomous AI agents using decentralized data.

---

If you need help — just ask.  
Happy building!!! 🚀

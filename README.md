# 🪙 Token Info Agent — Telegram bot powered by CoinGecko & DexScreener

Token Info Agent is a Telegram bot built as part of the Shade Agents Challenge (https://nearn.io/listing/make-a-token-info-agent). It answers natural language queries about cryptocurrency token prices in real-time using public APIs from CoinGecko and DexScreener.

---

# ⚙️ Features

- Understands natural language prompts such as:
  - “What’s the price of ETH?”
  - “How much is PEPE?”
  - “Price of SHIBA?”
- Fetches live prices from CoinGecko (primary source) and DexScreener (fallback)
- Replies directly inside Telegram chats
- Easy to deploy and extend in Python
- Uses `.env` file to store Telegram bot token securely

---

# 🧩 Prompt Examples (`prompt_examples.txt`)

1. What's the price of SOL?
→ 💰 SOL price is $178.42 (via CoinGecko)

2. How much is 1 ETH?
→ 💰 ETH price is $3078.12 (via CoinGecko)

3. Price of PEPE?
→ 💱 PEPE price is $0.00000124 (via DexScreener)

---

# 📦 Installation Instructions

1. Clone the repository

git clone https://github.com/pavave/token-info-agent-.git
cd token-info-agent


2. Create and activate a virtual environment (recommended)

python3 -m venv venv

source venv/bin/activate # Linux/MacOS

venv\Scripts\activate # Windows PowerShell


3. Install dependencies

pip install -r requirements.txt


---

# 🔐 Configuration

1. Create `.env` file

Copy the example environment file and fill in your Telegram bot token:

cp .env.example .env


Edit `.env` to add your actual token:

TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_API_KEY


---

# 🚀 Running the Bot

Run the bot script:

python main.py


---

# 💬 Usage

Open Telegram, find your bot by username, start chatting, and try queries like:

- What's the price of ETH?
- Price of SOL?
- How much is PEPE?

The bot will reply with live token price information fetched from CoinGecko or DexScreener.

---

# 📁 Project Structure

token-info-agent/

├── main.py # Telegram bot main logic and handlers

├── token_utils.py # Token price fetching logic (CoinGecko & DexScreener APIs)

├── requirements.txt # Python dependencies

├── .env.example # Example environment variable file

├── README.md # This README file

└── prompt_examples.txt # Example user prompts and expected outputs


---

# 🎥 Demo Video

Watch demo video on YouTube (replace with actual link once available)

---

🛠 Technology Stack

- Python 3.8+
- python-telegram-bot library
- CoinGecko API (free, no API key required)
- DexScreener API (for DEX token prices)
- requests and python-dotenv for HTTP and environment management

---

# 🧠 Future Improvements Ideas

- Add currency conversion (e.g., ETH to EUR)
- Support batch queries (multiple tokens in one message)
- Implement price alerts and notifications
- Provide a simple web or CLI interface
- Integrate LLM for better natural language understanding

---

# 📜 License

This project is licensed under the MIT License — free to use, modify, and distribute.

---

# 🤖 About

Created as part of the Shade Agents initiative on the NEAR blockchain ecosystem, showcasing autonomous AI agents capable of working seamlessly with decentralized data and protocols.

---

If you have any questions or want help setting up, just ask!  
Happy coding! 🚀

import requests
import re

def extract_token_name(text):
    match = re.search(r"\b([A-Z0-9]{2,10})\b", text.upper())
    return match.group(1) if match else None

def get_from_coingecko(token):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={token.lower()}&vs_currencies=usd"
    try:
        res = requests.get(url)
        data = res.json()
        price = data.get(token.lower(), {}).get("usd")
        if price:
            return f"💰 {token} price is ${price:.4f} (via CoinGecko)"
    except:
        return None

def get_from_dexscreener(token):
    url = f"https://api.dexscreener.com/latest/dex/search/?q={token}"
    try:
        res = requests.get(url)
        data = res.json()
        pairs = data.get("pairs", [])
        if pairs:
            price = pairs[0].get("priceUsd")
            if price:
                return f"💱 {token} price is ${float(price):.6f} (via DexScreener)"
    except:
        return None

def get_token_price(text):
    token = extract_token_name(text)
    if not token:
        return "❌ Couldn't detect a token in your message."

    result = get_from_coingecko(token)
    if result:
        return result

    result = get_from_dexscreener(token)
    if result:
        return result

    return f"❓ Sorry, I couldn't find a price for {token}."

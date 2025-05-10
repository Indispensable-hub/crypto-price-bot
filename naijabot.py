import asyncio
import requests
from telegram import Bot
import time

print("Starting the crypto Bot....")


#Config
TOKEN = '7666081755:AAEtqEcNAiwY-z9UezlLd_9eB4VSrCY1o08'
USER_ID = 6367015862
ALERT_PRICE = 103280 #SET YOUR ALERT PRICE 103,163.60USD

bot = Bot(token=TOKEN)

def get_btc_price():
    print("Fetching BTC price...")
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    response = requests.get(url)
    data = response.json()
    print("BTC price is Fetched.")
    return data['bitcoin']['usd']

async def send_alert(price):
    message = f"Bitcoin Alert! Current price is ${price}"
    print(f"Sending Telegram alert: {message}")
    await bot.send_message(chat_id=USER_ID, text=message)
    
#loop to check price every 60 seconds
async def main():
    print("Bot is now watching BTC...")
    try:
        while True:
            price = get_btc_price()
            print(f"Current BTC Price: ${price}")
            if price >= ALERT_PRICE:
                await send_alert(price)
                break
            await asyncio.sleep(60)
    except Exception as e:
            print(f"Runtime Error: {e}")
            await asyncio.sleep(60)
            
            
print("Preparing tp run main()")
       
if __name__ == "__main__":
    print("About to start asyncio")
    asyncio.run(main())
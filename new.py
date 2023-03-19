from telethon import TelegramClient, sync, events
from functions import *
from variables import *
import time

api_id = '29309659'
api_hash = 'adf52a11331f660354976065c2a3d06f'
chatname = 'binomo_options_trade'
# chatname = 'Trading_Binomo_Signals_Tips'
# chatname = 'testaccess1'

# Replace YOUR_API_ID and YOUR_API_HASH with your Telegram API ID and hash
client = TelegramClient('test', api_id, api_hash)

# Connect to Telegram
client.start()


def getLastId():
    messages = client.get_messages(chatname, limit=1)
    for message in messages:
        print("Last Id Retrieved")
        return message.id


last_id = getLastId()

balance = get_balance()

print("\n============================================\n")
print("TradeBot Started")
print(f"\n{'STARTING BALANCE:':20}", '₹ '
      f'{balance:,}')
print("\n============================================\n")

while True:
    new_messages = client.get_messages(chatname, limit=1)
    for message in new_messages:
        if (message.id > last_id):
            last_id = last_id + 1
            if message.message.find("\"DOWN\"") != -1:
                print("\nTime - " + datetime.now().strftime("%H:%M:%S"))
                print("SIGNAL RECEIVED - SELL\n\n")
                print("Before Balance : ₹ " + str(get_balance()))
                setTime()
                pointer_click(SELL)
                time.sleep(0.5)
                print("After Balance : ₹ " + str(get_balance()))

            elif message.message.find("\"UP\"") != -1:
                print("\nTime - " + datetime.now().strftime("%H:%M:%S"))
                print("SIGNAL RECEIVED - BUY\n\n")
                print("Before Balance : ₹ " + str(get_balance()))
                setTime()
                pointer_click(BUY)
                time.sleep(0.5)
                print("After Balance : ₹ " + str(get_balance()))
            else:
                print("\n" + " - " + message.message + "\n\n- " + nowTime())

    time.sleep(1)
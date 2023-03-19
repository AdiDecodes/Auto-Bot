from functions import *
from variables import *
import pyperclip
from telethon import TelegramClient, events, sync


def init():
    api_id = '29309659'
    api_hash = 'adf52a11331f660354976065c2a3d06f'
    client = TelegramClient('adityasingh_1', api_id, api_hash).start()
    chatname = 'binomo_options_trade'
    return chatname, client


balance = get_balance()

print("\n============================================\n")
print("TradeBot Started")
print(f"\n{'STARTING BALANCE:':20}", '₹ '
      f'{balance:,}')
print("\n============================================\n")

chatname, client = init()


@client.on(events.NewMessage(chats=chatname))
async def handler(event):
    if event.text.find("\"DOWN\"") != -1:
        print("\nTime - " + datetime.now().strftime("%H:%M:%S"))
        print("SIGNAL RECEIVED - SELL\n\n")
        print("Before Balance : ₹ " + str(get_balance()))
        setTime()
        pointer_click(SELL)
        time.sleep(0.5)
        print("After Balance : ₹ " + str(get_balance()))

    elif event.text.find("\"UP\"") != -1:
        print("\nTime - " + datetime.now().strftime("%H:%M:%S"))
        print("SIGNAL RECEIVED - BUY\n\n")
        print("Before Balance : ₹ " + str(get_balance()))
        setTime()
        pointer_click(BUY)
        time.sleep(0.5)
        print("After Balance : ₹ " + str(get_balance()))
    else:
        print(event.text)


client.loop.run_forever()
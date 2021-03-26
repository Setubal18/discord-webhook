from flask import Flask
# from modules.webhook import send
import asyncio
import logging
from discord_webhook import DiscordWebhook
from config import URL
import logging

logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)

class AsyncDiscord():
    def __init__(self):
        pass
        #asyncio.set_event_loop(asyncio.new_event_loop())
        #self.loop = asyncio.get_event_loop()

    def send(self, method):
        asyncio.set_event_loop(asyncio.new_event_loop())
        self.loop = asyncio.get_event_loop()
        r =  self.loop.run_until_complete(method())
        return r


@app.route('/push', methods=['GET', 'POST'])
def push():
    logging.info('hello def')
    asyncDis = AsyncDiscord()
    res = asyncDis.send(send1)
    logging.info('result', res.__dict__)
    # result = False
    if (res == 200):
        return f'<h1>Sucesso {res}</h1>'
    else:
        return '<h1>Error</h1>'

def send1():
    logging.info('send')
    webhook = DiscordWebhook(url=URL, content='Webhook Message')
    response = webhook.execute()
    logging.debug('response', response.status_code)
    print('response', response.status_code)
    return response



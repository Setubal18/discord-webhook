from flask import Flask
from modules.webhook import send
import asyncio
import logging

logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/push',methods=['GET', 'POST'])
def push():
    asyncio.set_event_loop(asyncio.new_event_loop())
    logging.info('hello def')
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(send())
    logging.info('result',result)
    #result = False
    if (result == 200):
        return f'<h1>Sucesso {result}</h1>'
    else:
        return '<h1>Error</h1>'

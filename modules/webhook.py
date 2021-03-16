import asyncio
from discord_webhook import DiscordWebhook
from config import URL
import logging
async def send():
    logging.info('send')
    webhook = DiscordWebhook(url=URL, content='Webhook Message')
    #response = webhook.execute()
    return webhook.execute()


import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

channel1id = int(os.getenv('ID1'))
channel2id = int(os.getenv('ID2'))


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.channel.id == channel1id:
        channeltosend = client.get_channel(channel2id)
        if channeltosend:
            await channeltosend.send(message.content)

keep_alive()
client.run(os.getenv('TOKEN'))

import discord
import os
from keep_alive import keep_alive

client = discord.Client()
channel1id = os.getenv('ID1')
channel2id = os.getenv('ID2')


@client.event
async def on_ready():
    print("Bot is ready")


@client.event
async def on_message(message):
    if message.channel.id == channel1id:
        channeltosend = client.get_channel(channel2id)
        await channeltosend.send(message.content, embed=message.embeds[0])


keep_alive()
client.run(os.getenv('TOKEN'))

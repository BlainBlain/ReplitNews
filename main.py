import discord
import os
import asyncio
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
            try:
                await channeltosend.send(message.content, embed=message.embeds[0])
            except discord.HTTPException as e:
                if e.status == 429:
                    retry_after = e.retry_after
                    print(f"Rate limit hit. Retrying after {retry_after} seconds.")
                    await asyncio.sleep(retry_after)
                    await channeltosend.send(message.content, embed=message.embeds[0])


keep_alive()
client.run(os.getenv('TOKEN'))

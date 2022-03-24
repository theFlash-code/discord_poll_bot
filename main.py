import discord
import os
import requests
import json
import asyncio
# from replit import db
from keep_alive import keep_alive


client = discord.Client()

def deal_with_poll(poll):
  pollSplit = poll.split('?', 1)
  question = pollSplit[0]
  option = pollSplit[1].split('/')
  pollMessage = question+"?"
  for i in range(1,len(option)):
    pollMessage += "\n\n"+emojis[i]+" "+option[i]
  return [pollMessage, len(option)]

number_emoji = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟']
emojis = ["{}\N{COMBINING ENCLOSING KEYCAP}".format(num) for num in range(0, 10)]

@client.event
async def on_ready():
  print("we have logged in as {0.user}".format(client))
  await client.get_channel(940613586030563392).send('poll bot is now online!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("$poll"):
    length = len(message.content)
    poll = message.content[5:length]
    pollMessage = deal_with_poll(poll)
    
    curMessage = message.channel.send(pollMessage[0])
    await curMessage
    await asyncio.sleep(0.1)
    last_message = await message.channel.fetch_message(
    message.channel.last_message_id)
    for i in range(1,pollMessage[1]):
      await last_message.add_reaction(emojis[i])

keep_alive()

client.run(os.environ['TOKEN'])
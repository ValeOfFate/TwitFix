from discord.ext import commands
import discord

BotToken = "MTEyNTY3MDcxNjAwMDQzNjMwNQ.G-mG7s.hEGEjBYdpK35xbg5Ute-YQTqBgg0ws0fn-e7CE"

# Bot Creation
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='^', intents=intents)

# Startup
@bot.event
async def on_ready():
    print('Bot OK')

# Value Check
@bot.event
async def on_message(message):
    if message.author == bot.user:
        if len(message.embeds) == 0:
            await message.edit(content="Given Link doesnt provide and fxtwitter embeds")
        return
    
    else:
        messageData =  message.content.lower()
        if "twitter.com" in messageData and "fxtwitter.com" not in messageData:
            messageData = messageData.replace("twitter.com", "fxtwitter.com", 1)
            await message.channel.send(messageData)
            return; 

    return 

# Token
bot.run(BotToken)

import discord 
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.event
async def on_ready():
        print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
          return
    if message.content.startswith('random'):
         await message.channel.send('Guess a number from 1 to 20')
    await bot.process_commands(message)

@bot.command()
async def randomnumber(ctx):
    random_num = random.randint(1, 20)
    await ctx.send(random_num)


bot.run("MTMzMzQ2ODIwMDk2MDI2MjMzNg.G0xZe6.zCv9wkkrMjjc3ZpHcDfW8A4cOFfXQJ-zV3CYXY")
import Joking
import discord
import random
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks

BOT_TOKEN = "MTE3MTU4NTIxMTMyMzEzODE1OQ.G0NY3_._B1EPBwmW-el7qg2ZThtnxCGjkyU1omIU5Q0OA"
CHANNEL_ID = 1171584985346617477

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello!")
    try:
        synced = await bot.tree.sync()
        print(f"{len(synced)} commands")
    except Exception as e:
        print(e)

    dad_joke.start()


@bot.tree.command(name="knockknock", description="knock knock joke")
async def knock(interaction: discord.Interaction):
    await interaction.response.send_message(Joking.Random_knock_knock_joke())


@bot.tree.command(name="swell", description="swell indicator")
async def swell(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!")

    
@bot.tree.command(name="roll")
async def roll(interaction: discord.Interaction):
    dice = random.randint(1, 6)
    await interaction.response.send_message(dice)


@tasks.loop(hours=1)
async def dad_joke():
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(Joking.random_dad_joke())

bot.run(BOT_TOKEN)

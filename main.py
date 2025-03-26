from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
from utils import ask_llm


load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)  # in milliseconds
    await ctx.send(f"Pong! Latency: {latency}ms")


@bot.command()
async def ask(ctx, *, query: str):
    async with ctx.typing():
        try:
            response = ask_llm(query)
            await ctx.send(response)
        except Exception as e:
            print(e)
            await ctx.send("Sorry something went wrong. Please try again later.😒")


bot.run(TOKEN)

import os
import string

import discord
import dotenv
from discord import Option

dotenv.load_dotenv()
bot = discord.Bot(
    debug_guilds=[746045840325345310]
)

@bot.event
async def on_ready():
    print("Der Bot wurde gestartet")

@bot.slash_command(description="Sends the bot's latency.")
async def verwarnung(ctx, user: Option(discord.Member, "Der zu verwarnende Nutzer"), message: Option(discord.SlashCommandOptionType.string, "Der Grund für die Verwarnung")):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.yellow()
    )
    embed_message = "**======================================================\n\nTEAMVERWARNUNG\n\nName | **{0}**\nGrund | **{1}**\n\n======================================================**"
    embed.add_field(name="", value=embed_message.format(user.mention, message))
    await ctx.respond("", embed=embed)

bot.run(os.getenv('TOKEN'))
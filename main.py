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

@bot.slash_command(description="Verwarnt ein Teammitglied")
async def verwarnung(ctx, user: Option(discord.Member, "Der zu verwarnende Nutzer"), message: Option(discord.SlashCommandOptionType.string, "Der Grund für die Verwarnung")):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.yellow()
    )
    embed_message = "**======================================================\n\nTEAMVERWARNUNG\n\nName | **{0}**\nGrund | **{1}**\n\n======================================================**"
    embed.add_field(name="", value=embed_message.format(user.mention, message))
    await ctx.respond("", embed=embed)

@bot.slash_command(description="Updatet die Rolle eines Teammitglieds")
async def rollenupdate(ctx, user: Option(discord.Member, "Der betroffene Nutzer"), role_old: Option(discord.Role, "Die alte Rolle"), role_new: Option(discord.Role, "Die neue Rolle")):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.green()
    )
    embed_message = "**======================================================\n\nTEAMUPDATE\n\n{0} hat nun den Rang {1}\n\nName | {0}\nAlter Rang | {2}\nNeuer Rang | {1}\n\n======================================================**"
    embed.add_field(name="", value=embed_message.format(user.mention, role_new.mention, role_old.mention))
    await user.remove_roles(role_old)
    await user.add_roles(role_new)
    await ctx.respond("", embed=embed)

bot.run(os.getenv('TOKEN'))
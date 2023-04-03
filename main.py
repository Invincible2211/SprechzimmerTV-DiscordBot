import os
import string

import discord
import dotenv
from discord import Option, guild

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

@bot.slash_command(description="Nimmt einen User in das Team auf")
async def beitritt(ctx, user: Option(discord.Member, "Der betroffene Nutzer"), role: Option(discord.Role, "Die neue Rolle")):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.dark_green()
    )
    embed_message = "**======================================================\n\nTEAMUPDATE\n\n{0} wurde als {1} ins Server-Team aufgenommen!\n\n======================================================**"
    embed.add_field(name="", value=embed_message.format(user.mention, role.mention))
    await user.add_roles(role)
    await ctx.respond("", embed=embed)

@bot.slash_command(description="Nimmt einen User in das Team auf")
async def teamkick(ctx, user: Option(discord.Member, "Der betroffene Nutzer")):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.dark_green()
    )
    embed_message = "**======================================================\n\nTEAMUPDATE\n\n{0} hat das Serverteam Verlassen\nWir wünschen dir viel Erfolg auf deinem weiteren weg,\nund danken dir für deine Geleistete Arbeit!\n\n======================================================**"
    embed.add_field(name="", value=embed_message.format(user.mention))
    await ctx.respond("", embed=embed)
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="ADMIN"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="DEVELOPER"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="TEST-DEVELOPER"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="SR.MODERATOR"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="MODERATOR"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="SUPPORTER"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="T-SUPPORTER"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="BUILDER"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Server-Team"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="SUPPORT"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="[Ticket] SUPPORT"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="[Ticket] BEWERBUNGEN"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="[Ticket] CITYBUILD"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="[Ticket] SKYBLOCK"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="[Ticket] SURVIVAL"))
    await user.remove_roles(discord.utils.get(ctx.guild.roles, name="MEDIA TEAM"))

bot.run(os.getenv('TOKEN'))
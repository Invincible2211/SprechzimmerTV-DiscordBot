import json
import os

import discord
import dotenv
from discord import Option, Interaction

with open('config.json', encoding='UTF-8') as data:
    config_data_json = json.load(data)
    config_data_string = json.dumps(config_data_json).encode('utf8')
    config = json.loads(config_data_string)

dotenv.load_dotenv()
bot = discord.Bot()


class AnnounceModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            discord.ui.InputText(
                label="Ankündigungstext",
                style=discord.InputTextStyle.long
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction: Interaction):
        embed = discord.Embed(
            title="ANKÜNDIGUNG",
            color=discord.Colour.dark_blue()
        )
        embed.add_field(name="", value=self.children[0].value)
        await interaction.response.send_message(embed=embed)


@bot.event
async def on_ready():
    print("Der Bot ist gestartet")


@bot.slash_command(description=config['commands']['warn']['description'])
async def verwarnung(ctx,
                     user: Option(discord.Member,
                                  config['commands']['warn']['argument_description']['user']),
                     message: Option(discord.SlashCommandOptionType.string,
                                     config['commands']['warn']['argument_description']['message'])):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.yellow()
    )
    embed.add_field(name="", value=config['commands']['warn']['message'].format(user.mention, message))
    await ctx.respond("", embed=embed)


@bot.slash_command(description=config['commands']['role_update']['description'])
async def rollenupdate(ctx,
                       user: Option(discord.Member,
                                    config['commands']['role_update']['argument_description']['user']),
                       role_old: Option(discord.Role,
                                        config['commands']['role_update']['argument_description']['old_role']),
                       role_new: Option(discord.Role,
                                        config['commands']['role_update']['argument_description']['new_role'])):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.green()
    )
    embed.add_field(name="", value=config['commands']['role_update']['message'].format(user.mention, role_new.mention,
                                                                                       role_old.mention))
    try:
        await user.remove_roles(role_old)
        await user.add_roles(role_new)
    except discord.Forbidden as e:
        print(e)
        ctx.respond(config['commands']['role_update']['error_message'].format(role_new.mention, role_old.mention))
        return
    await ctx.respond("", embed=embed)


@bot.slash_command(description=config['commands']['team_join']['description'])
async def beitritt(ctx,
                   user: Option(discord.Member,
                                config['commands']['team_join']['argument_description']['user']),
                   role: Option(discord.Role,
                                config['commands']['team_join']['argument_description']['role'])):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.dark_green()
    )
    embed.add_field(name="", value=config['commands']['team_join']['message'].format(user.mention, role.mention))
    try:
        await user.add_roles(role)
    except discord.Forbidden as e:
        print(e)
        ctx.respond(config['commands']['team_join']['error_message'].format(role.mention))
        return
    await ctx.respond("", embed=embed)


@bot.slash_command(description=config['commands']['team_kick']['description'])
async def teamkick(ctx,
                   user: Option(discord.Member,
                                config['commands']['team_kick']['argument_description']['user'])):
    embed = discord.Embed(
        title="TEAM | Team-Information",
        color=discord.Colour.red()
    )
    embed.add_field(name="", value=config['commands']['team_kick']['message'].format(user.mention))
    await ctx.respond("", embed=embed)
    try:
        for role_string in config['team_roles']:
            await user.remove_roles(discord.utils.get(ctx.guild.roles, name=role_string))
    except discord.Forbidden as e:
        print(e)
        ctx.respond(config['commands']['team_kick']['error_message'])


@bot.slash_command(description=config['commands']['announce']['description'])
async def announce(ctx):
    modal = AnnounceModal(title="Erstellen einer Ankündigung")
    await ctx.send_modal(modal)


bot.run(os.getenv('TOKEN'))

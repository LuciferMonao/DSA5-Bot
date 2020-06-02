# bot.py
import os
import random
import discord
from dotenv import load_dotenv

from discord.ext import commands

bot = commands.Bot(command_prefix=">")

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()




#EVENTS
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f"{client.user} has connected to Discord!")
    print(f"{guild.name} with the guild id {guild.id} is the churrent guild.")
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
@bot.event #Used to replay that users dont have the required permissions to issue a command.

async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the required role for this command.')

@bot.event
async def on_member_join(member):

    guild = discord.utils.get(bot.guilds, name=GUILD)

    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the {guild.name} Discord server!'
    )




#GENERAL COMMANDS
@bot.command(name="info", help="Shows more info regarding the bot.")
async def help(ctx):
    help_message = ("""
        Hello. This is the info interface of the DSA5 Bot.\nIts callable by issuing the command >info\nTo get more help regarding different groups of commands please use:\n>help-roll\n>help-info\n>help-bot\nThis bot was created by Nathan Zumbusch and stands under the GNU General Licence.\nTo contact the author, send an mail to lucifermonao@gmx.de.
        """)
    await ctx.send(help_message)

@bot.command(name="stop", help="Stops the bot Programm remotely.")
@commands.has_role("Developer")
async def stop(ctx):
    await ctx.send("Stopping bot programm...")
    exit()





#ROLL
@bot.command(name="roll", help="Rolls a certain amount of dice.")
async def roll(ctx, dice: str):
    number_of_dice = dice[0]
    type_of_dice = dice[1]
    size_of_dice = dice[2:]
    print(f"Rolling {number_of_dice} dice with the type {type_of_dice} and the options {size_of_dice}")
    if str(type_of_dice).upper() == "D" or str(type_of_dice).upper() == "W": 
        print("Normal roll...")
        results = []
        for roll in range(number_of_dice):
            results.append(str(random.randint(0, size_of_dice + 1)))
            print(roll)
        print(results)
    elif str(type_of_dice).upper() == "e": 
        print("Extended roll...")
        results = []
        for roll in range(number_of_dice):
            results.append(str(random.random(size_of_dice.split())))
            print(roll)
        
    await ctx.send(", ".join(results))
    print(f"Rolled {results}")



@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise







bot.run(TOKEN)

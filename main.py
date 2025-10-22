import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#Specify the permissions/intents for the bot:
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#How to call for the bot:
bot = commands.Bot(command_prefix='!', intents=intents)

#roles:
role_1 = "fiaper"
secret_role = "Gamer"

@bot.event
async def on_ready():
    print(f"Bot loaded and ready to go, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    

    await bot.process_commands(message) #DO NOT DELETE, this allows the bot to continue to proccess all of the other messages.

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name=role_1)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned to {role_1}")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles, name=role_1)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} has had the '{role_1}' role removed")
    else:
        await ctx.send("Role doesn't exist")

@bot.command()
@commands.has_role(role_1)
async def secret(ctx):
    await ctx.send("Welcome to the club!")

@secret.error
async def secret_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have permission to do that!")
        

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

#roles:
role_1 = "fiaper"
secret_role = "Gamer"
role_svbooster = "Server Booster"
role_verificated = "Verified"

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

#Specify the permissions/intents for the bot:
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#How to call for the bot:
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Bot loaded and ready to go, {bot.user.name}")

# Events:

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def premium_subscriptions(member, ctx):
    role_booster = discord.utils.get(ctx.guild.roles, name=role_svbooster)
    await member.send(f"{member.name} is boosting the server!")
    await ctx.author.add_roles(role_booster)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    #DO NOT DELETE, this allows the bot to continue to proccess all of the other messages.
    await bot.process_commands(message)  

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def dm(ctx, *, msg):
    await ctx.author.send(f"You said {msg} ")

@bot.command()
async def poll(ctx, *, question):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_readction("✅")
    await poll_message.add_readction("⛔")




#Verify Modal:
class VerifyModal(discord.ui.Modal, title="Verify"):
    verify_name = discord.ui.TextInput(
        label="NAME",
        placeholder="wagner Stefano",
        required=True,
        max_length=50
    )
    minecraft = discord.ui.TextInput(
        label="Play's Minecraft",
        placeholder="y/n",
        required=True,
        max_length=3
    )
    pokemongo = discord.ui.TextInput(
        label="Play's PokemonGo",
        placeholder="y/n",
        required=True,
        max_length=3
    )
    pokemongo_tc = discord.ui.TextInput(
        label="Trainer Code",
        placeholder="2074 5588 0748",
        required=False,
        max_length=14
    )
    institution = discord.ui.TextInput(
        label="School/Work",
        placeholder="eg. FIAP",
        required=True,
        max_length=25,
        style=discord.TextStyle.paragraph
    )


    async def on_submit(self, interaction: discord.Interaction):
        role_verificated = "Verified"
        role_verify = discord.utils.get(interaction.guild.roles, name=role_verificated)
        await interaction.user.add_roles(role_verify)
        await interaction.response.send_message(
            f"welcome to the server!\n**Name:** {self.verify_name.value}\n**Play's Minecraft:** {self.minecraft.value}\n**Play's PokemonGo:** {self.pokemongo.value}\n**PokemonGo Trainer-Code:** {self.pokemongo_tc.value or 'N/A'}\n**School:** {self.institution.value}",
            ephemeral=True
        )

@bot.tree.command(name="verify", description="Verify to access the server")
async def verify(interaction: discord.Interaction):
    role_verificated = "Verified"  # must match the same name above
    role_verify = discord.utils.get(interaction.guild.roles, name=role_verificated)

    if role_verify in interaction.user.roles:
        await interaction.response.send_message(
            f"{interaction.user.mention}, you are already verified!",
            ephemeral=True
        )
    else:
        modal = VerifyModal()
        await interaction.response.send_modal(modal)




# Report Modal:
class ReportModal(discord.ui.Modal, title="Report Form"):
    user_name = discord.ui.TextInput(
        label="USER'S DISCORD NAME",
        placeholder="eg. VampiroDoidão#0000",
        required=True,
        max_length=100
    )
    user_id = discord.ui.TextInput(
        label="USER'S DISCORD ID",
        placeholder="Make sure Developer mode is ON.",
        required=True,
        max_length=100
    )
    description = discord.ui.TextInput(
        label="Description",
        placeholder="eg. Broke rule #1",
        required=True,
        max_length=400,
        style=discord.TextStyle.paragraph
    )


    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f"✅ Report received!\n**Name:** {self.user_name.value}\n**Description:** {self.description.value}\n**User ID:** {self.user_id.value}",
            ephemeral=True
        )

@bot.tree.command(name="report", description="Report someone for bad behaviours")
async def report(interaction: discord.Interaction):
    modal = ReportModal()
    await interaction.response.send_modal(modal)


### Roles c.r.u.d

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
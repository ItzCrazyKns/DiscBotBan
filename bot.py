import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))
    
    print("Ready")

@client.command()
async def hello(ctx):
    await ctx.reply('Hello')
    
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)  
    
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)       
    
    

client.run('OTE4NzIwMjE4NTkzODg2Mjg4.YbLW4Q.jfmHO1UYbbJv4ekYlUnM4nbqT1U')

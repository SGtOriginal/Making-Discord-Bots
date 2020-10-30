import discord
from discord.ext import commands
from random import choice

client = commands.Bot(command_prefix = 'Put your bot prefix here')

@client.event
async def on_ready():
    print('Booted up...................\nUploading files to remote server............\nFiles upload complete!\nBot ready to start!\nStarting bot in.....5.....4.....3.....2.....1......0\nBot started!!!!!')

@client.event
async def on_member_join(member):
    print(f'Hello, {member}, we hope you have a good time!')

@client.event
async def on_member_remove(member):
    print(f'{member} has left. Bye!')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def hello(ctx):
    await ctx.send(f'Hi!')

@client.command()
async def helpme(ctx):
    await ctx.send(f'Here is the list of commands: <helpme <ping <hello')

@client.command()
@commands.has_permissions(manage_messages = True)
async def ClearMSG(ctx):
    await ctx.channel.purge(limit=10000)
    await ctx.send(f'Channel cleared!')
  
client.run('Paste bot token here')

import discord
#from discord.ext.commands import Bot
from discord.ext import commands
from random import choice
import shutil
from discord.utils import get
import os
from os import system
import asyncio

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

@client.command(
	help="Uses come crazy logic to determine if pong is actually the correct value or not.",
	brief="Prints pong back to the channel."
)

async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def hello(ctx):
    await ctx.send(f'Hi!')

@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx):
    await ctx.channel.purge(limit=10000)
    await ctx.send(f'Channel cleared!')

@client.command(
	help="Changes the nickname to 'You got trolled'",
	brief="The name says it all."
)
async def troll(ctx, member : discord.Member):
    await member.edit(nick="You got trolled!")
    
@client.command(
	help="Add numbers.",
	brief="Add numbers."
)
async def add(ctx, a: int, b: int):
	await ctx.send(a + b)
	
@client.command(
	help="Subtract numbers.",
	brief="Subtract numbers."
)
async def sub(ctx, a: int, b: int):
	await ctx.send(a - b)
	
@client.command(
	help="Multiplies numbers.",
	brief="Multiplies numbers."
)
async def mul(ctx, a: int, b: int):
	await ctx.send(a * b)

@client.command(
	help="Divide numbers like this.",
	brief="Divide numbers like this."
)
async def div(ctx, a: int, b: int):
	await ctx.send(a / b)
  
client.run('Paste bot token here')

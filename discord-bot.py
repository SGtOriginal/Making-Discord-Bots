import random
import discord
from discord.ext import commands
import asyncio
from keep_alive import keep_alive

client = commands.Bot(command_prefix = 'Your Preferred Bot Prefix')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Enter Any Random Here'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

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
async def clear(ctx, a: int):
    await ctx.channel.purge(limit=1 + a)
    await ctx.send(f'Channel cleared!')

@client.command(
	help="Changes the nickname.",
	brief="The name says it all."
)
async def nick(ctx, member : discord.Member, args):
  
  await member.edit(nick=args)
    
  await ctx.send(f'Nickname changed.')
	
@client.command(
	help="Looks like you need some help, lol.",
	brief="Prints the list of values back to the channel."
)
async def print(ctx, *args):
	response = ""

	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)

@client.command(
	help="Add numbers like this 'add 10 20'.",
	brief="Add numbers like this 'add 10 20'."
)
async def add(ctx, a: int, b: int):
	await ctx.send(a + b)
	
@client.command(
	help="Subtract numbers like this 'sub 10 20'.",
	brief="Subtract numbers like this 'sub 10 20'."
)
async def sub(ctx, a: int, b: int):
	await ctx.send(a - b)
	
@client.command(
	help="Multiplies numbers like this 'mul 10 20'.",
	brief="Multiplies numbers like this 'mul 10 20'."
)
async def mul(ctx, a: int, b: int):
	await ctx.send(a * b)

@client.command(
	help="Divide numbers like this 'div 10 20'.",
	brief="Divide numbers like this 'div 10 20'."
)
async def div(ctx, a: int, b: int):
	await ctx.send(a / b)

@client.command(
        help="Chooses between two options.",
        brief="Chooses between two options."
)
async def choose(ctx, a: str, b: str):
        list1 = [a, b]
        await ctx.send(random.choice(list1))

keep_alive()

client.run('Paste Bot Token Here')

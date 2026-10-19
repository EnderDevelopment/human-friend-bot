import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='follow', help='Follow a designated player')
async def follow(ctx, player_name: str):
    # Logic to follow the designated player
    await ctx.send(f'Following {player_name}!')

@bot.command(name='emote', help='Dance with the given emote number (1-8)')
async def emote(ctx, emote_number: int):
    if 1 <= emote_number <= 8:
        # Logic to perform the dance move
        await ctx.send(f'Performing emote {emote_number}!')
    else:
        await ctx.send('Please provide a valid emote number between 1 and 8.')

@bot.command(name='jump', help='Jump to pass through obstacles')
async def jump(ctx):
    # Logic to jump
    await ctx.send('Jumping!')

@bot.command(name='list_players', help='List all players in the UI')
async def list_players(ctx):
    # Logic to list players
    players = ['Player1', 'Player2', 'Player3']  # Example list of players
    await ctx.send('List of players: ' + ', '.join(players))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.lower() == 'hello!':
        await message.channel.send('hi!')
    
    await bot.process_commands(message)

bot.run(TOKEN)
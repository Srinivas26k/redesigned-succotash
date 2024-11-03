import discord
from discord.ext import commands
import aiohttp
import json
import os
import asyncio
import logging
import traceback
from ollama import Client as OllamaClient
from dotenv import load_dotenv
from github_integration import setup as setup_github

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('studybuddy_bot')

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

# Ollama client
ollama_client = OllamaClient()

# Gemini API setup
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent'

async def query_gemini(prompt):
    async with aiohttp.ClientSession() as session:
        headers = {
            'Content-Type': 'application/json',
            'x-goog-api-key': GEMINI_API_KEY
        }
        data = {
            'contents': [{'parts': [{'text': prompt}]}]
        }
        async with session.post(GEMINI_API_URL, headers=headers, json=data) as response:
            result = await response.json()
            return result['candidates'][0]['content']['parts'][0]['text']

@bot.event
async def on_ready():
    logger.info(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        logger.info(f"Connected to server: {guild.name} (id: {guild.id})")
    await bot.change_presence(activity=discord.Game(name="Studying with AI"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    logger.info(f"Message received: {message.content} from {message.author}")
    await bot.process_commands(message)

@bot.command()
async def quick(ctx, *, query):
    """Quick response using Ollama"""
    logger.info(f"Quick command received: {query}")
    try:
        await ctx.typing()
        await asyncio.sleep(1)
        logger.info("Attempting to generate response with llama3.2")
        response = ollama_client.generate(model='llama3.2', prompt=query)
        logger.info(f"Response generated: {response['response'][:50]}...")  # Log first 50 chars of response
        await ctx.send(response['response'])
        logger.info("Quick command response sent")
    except Exception as e:
        error_message = f"An error occurred: {str(e)}"
        await ctx.send(error_message)
        logger.error(f"Error in quick command: {error_message}")
        logger.error(f"Full traceback: {traceback.format_exc()}")

@bot.command()
async def deep(ctx, *, query):
    """Deep analysis using Gemini 1.5 Pro"""
    logger.info(f"Deep command received: {query}")
    try:
        await ctx.typing()
        response = await query_gemini(query)
        await ctx.send(response)
        logger.info("Deep command response sent")
    except Exception as e:
        error_message = f"An error occurred with Gemini API: {str(e)}"
        await ctx.send(error_message)
        logger.error(f"Error in deep command: {error_message}")
        logger.error(f"Full traceback: {traceback.format_exc()}")

@bot.command(name='studybuddy_help')
async def studybuddy_help(ctx):
    """Display help information"""
    help_text = """
    StudyBuddy AI Commands:
    !quick [query] - Get a quick response using local AI
    !deep [query] - Get a more detailed response using cloud AI
    !studybuddy_help - Display this help message
    """
    await ctx.send(help_text)
    logger.info("Help command executed")

setup_github(bot)

bot.run(os.getenv('DISCORD_TOKEN'))
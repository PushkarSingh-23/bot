import discord
from discord.ext import commands
import openai
import nest_asyncio
import asyncio

# Set up your OpenAI API credentials
openai.api_key = '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'

# Allow running nested event loops in Colab
nest_asyncio.apply()

# Create an instance of the Discord bot with intents
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Event handler for when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command to ask a question
@bot.command(name='prabhu')
async def ask_question(ctx, *, question):
    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose the appropriate engine
        prompt=f'Question: {question}\nAnswer:',
        max_tokens=500,  # Adjust the response length as needed
        n=1,
        stop=None,
        temperature=0.7  # Adjust the temperature to control response randomness
    )

    # Extract the generated answer from the API response
    answer = response.choices[0].text.strip()

    # Send the answer back to the user
    await ctx.send(answer)

# Define a function to start the bot
async def start_bot():
    bot_token = 'OTQxMzk2MzAwODUzODA5MTky.GkAaE3.dvgudNbStTyN80_5hu1N4spdyzEx3Lz46qufbw'
    await bot.start(bot_token)

# Run the bot
asyncio.run(start_bot())

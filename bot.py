import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Dictionary to keep track of running Pomodoros per user
active_pomodoros = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def pomodoro(ctx, minutes: int = 25):
    user_id = ctx.author.id
    
    if user_id in active_pomodoros:
        await ctx.send("❌ You already have a Pomodoro running! Use `!cancelpomodoro` to stop it first.")
        return

    await ctx.send(f"⏳ Pomodoro started for {minutes} minutes! Focus time begins now...")

    # Create an asyncio task and store it
    task = asyncio.create_task(pomodoro_timer(ctx, minutes))
    active_pomodoros[user_id] = task

async def pomodoro_timer(ctx, minutes):
    user_id = ctx.author.id
    try:
        await asyncio.sleep(minutes * 60)
        await ctx.send(f"✅ {ctx.author.mention}, Time’s up! Take a break ☕")
    except asyncio.CancelledError:
        await ctx.send(f"❌ {ctx.author.mention}, your Pomodoro was cancelled.")
    finally:
        # Remove from active dictionary
        active_pomodoros.pop(user_id, None)

@bot.command()
async def cancelpomodoro(ctx):
    user_id = ctx.author.id
    task = active_pomodoros.get(user_id)
    
    if task:
        task.cancel()
    else:
        await ctx.send("You don't have an active Pomodoro running.")

bot.run("MY_TOKEN")

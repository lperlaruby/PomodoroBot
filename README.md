# PomodoroBot

Discord bot for Pomodoro timers.

## What it does

- Start timers (default 25 minutes, or pick your own time)
- One timer per person
- Cancel timers if needed
- Tells you when time's up

## You need

- Python 3.7+
- Discord bot token
- discord.py

## Setup

### 1. Install discord.py

```bash
pip install discord.py
```

### 2. Get bot token

1. Go to https://discord.com/developers/applications
2. Click "New Application" 
3. Go to "Bot" tab
4. Click "Add Bot"
5. Copy the token

### 3. Put your token in bot.py

Replace line 52 with your token:
```python
bot.run("your_token_here")
```

### 4. Add bot to server

1. In Discord Developer Portal, go to OAuth2 > URL Generator
2. Check "bot" 
3. Check permissions: Send Messages, Read Message History
4. Copy the URL and open it
5. Pick your server

### 5. Run it

```bash
python bot.py
```

## Commands

Use `!` before each command:

**`!pomodoro`** - Start 25 minute timer
**`!pomodoro 15`** - Start custom timer (15 minutes)
**`!cancelpomodoro`** - Stop your timer

## Examples

```
!pomodoro
⏳ Pomodoro started for 25 minutes! Focus time begins now...

[25 minutes later]
✅ @you, Time's up! Take a break ☕
```

```
!pomodoro 10
⏳ Pomodoro started for 10 minutes! Focus time begins now...

!cancelpomodoro  
❌ @you, your Pomodoro was cancelled.
```
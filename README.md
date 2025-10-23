# 🤖 Discord Bot

A simple C.R.U.D. bot built in Python.

This bot welcomes new members, assigns and removes roles via commands, and restricts access to a secret command based on role permissions.

---

## 📋 Table of Contents

- [How It Works](#notebook-how-it-works)  
- [Features](#features)  
- [Example Commands](#example-commands)  
- [Setup Instructions](#wrench-setup-instructions)  

---

## :notebook: How It Works

Once added to a Discord server, the bot does the following:

- Sends a **private welcome message** to users who join the server.
- Allows users to **assign or remove** themselves from a specific role using commands.
- Restricts a "secret" command only to users who have the required role.
- Logs all activity to `discord.log` for debugging or auditing.

The bot uses Discord intents to handle messages and member events, and reads your token securely using `.env`.

---

## 🚀 Features

- ✅ Welcome DMs for new members  
- ✅ Command to assign a predefined role  
- ✅ Command to remove that role  
- ✅ Restricted access to commands using role-based permissions  
- ✅ Logs stored to `discord.log`  
- ✅ Easy-to-read, beginner-friendly Python code  
- ✅ Built using `discord.py` and `dotenv`  

---

## ⚡ Example Commands

| Command      | Description                            | Example                  |
|--------------|----------------------------------------|--------------------------|
| `!hello`     | Says hello to the user                 | `!hello`                 |
| `!assign`    | Assigns the user the `fiaper` role     | `!assign`                |
| `!remove`    | Removes the `fiaper` role from user    | `!remove`                |
| `!secret`    | Only usable if user has the `fiaper` role | `!secret`             |

---

## 🔧 Setup Instructions

1. **Clone the repo or copy the code:**

```bash
git clone https://github.com/yourusername/discord-role-bot.git
cd discord-role-bot
```

2. **Install Dependencies:**

```
pip install -r requirements.txt
```

3. Update the .env file with your token:
```
DISCORD_TOKEN=your_bot_token_here
```

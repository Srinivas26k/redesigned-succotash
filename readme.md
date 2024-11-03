Here’s a detailed `README.md` file for your **StudyBuddy AI** Discord bot, structured step-by-step for easy setup and use:

---
(#https://discord.gg/KNYetyMw)
# StudyBuddy AI 

StudyBuddy AI is a powerful Discord bot designed to assist students, researchers, coders, freelancers, and content creators with various tasks using AI-powered responses. It integrates both local and cloud-based AI models, offering quick answers, deep analyses, and GitHub functionality directly within Discord.

## Table of Contents

1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Setup Guide](#setup-guide)
4. [Bot Commands](#bot-commands)
5. [Troubleshooting](#troubleshooting)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **Quick Responses**: Fast, locally-processed answers using Ollama's Llama 3.2 model.
- **Deep Analysis**: Complex queries handled by Google’s Gemini 1.5 Pro API for in-depth responses.
- **GitHub Integration**: Search GitHub repositories and create gists from within Discord.
- **Error Handling**: Robust logging and error handling to streamline troubleshooting.
- **Message Splitting**: Automatically splits long responses to comply with Discord’s character limits.

---

## Prerequisites

Before getting started, make sure you have:

1. **Python 3.8+** installed.
2. **Discord Bot Token** from the [Discord Developer Portal](https://discord.com/developers/applications).
3. **Gemini API Key** for accessing cloud-based AI.
4. **GitHub Personal Access Token** for GitHub integration.
5. **Ollama** installed and running locally (for local AI responses).

---

## Setup Guide

### Step 1: Create and Set Up Your Project Folder

1. Open Visual Studio Code (VS Code).
2. Create a new folder for your project (e.g., `StudyBuddy-AI`).
3. Open this folder in VS Code.

### Step 2: Set Up a Virtual Environment

1. Open the VS Code terminal by navigating to **View > Terminal**.
2. Run the following command to create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

### Step 3: Install Required Packages

With the virtual environment activated, install the necessary packages:

```bash
pip install discord.py aiohttp ollama python-dotenv
```

### Step 4: Set Up Environment Variables

1. Create a `.env` file in the project folder.
2. Add your bot’s sensitive information to the `.env` file:

   ```plaintext
   DISCORD_TOKEN=your_discord_bot_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   GITHUB_TOKEN=your_github_token_here
   ```

3. Replace `your_discord_bot_token_here`, `your_gemini_api_key_here`, and `your_github_token_here` with your actual tokens and API keys.

### Step 5: Configure Your Bot Code for Environment Variables

In your bot’s main Python file (e.g., `study_buddy_bot.py`), import `dotenv` and load your environment variables at the beginning:

```python
from dotenv import load_dotenv
import os

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
```

### Step 6: Start the Ollama Server

Ollama must be running in a separate terminal window. Start it with the following command:

```bash
ollama serve
```

### Step 7: Run the Bot

In the VS Code terminal, start your bot by running:

```bash
python study_buddy_bot.py
```

Your bot should now be running and connected to Discord!

### Step 8: Invite the Bot to Your Server

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Select your bot application and navigate to **OAuth2 > URL Generator**.
3. Under **Scopes**, check "bot" and "applications.commands".
4. Under **Bot Permissions**, select:
   - Read Messages/View Channels
   - Send Messages
   - Use Slash Commands

5. Copy the generated URL, paste it in your browser, select your server, and authorize the bot.

---

## Bot Commands

Here’s a list of the available commands:

- **`!quick [query]`**: Get a quick response using the Llama 3.2 model via Ollama.
- **`!deep [query]`**: Get a detailed response from the Gemini 1.5 Pro API.
- **`!studybuddy_help`**: Display the help message with all available commands.
- **`!search_repo [query]`**: Search for GitHub repositories.
- **`!create_gist [content]`**: Create a GitHub gist with the specified content.

---

## Troubleshooting

If you run into issues, try these steps:

### 1. Bot Not Responding

- **Verify Bot Permissions**: Ensure the bot has the necessary permissions in your Discord server (e.g., "Read Messages/View Channels", "Send Messages").
- **Restart the Bot**: Stop the bot (Ctrl+C in the terminal) and restart it using `python study_buddy_bot.py`.
- **Reinvite the Bot**: In the Developer Portal, generate a new invite link with proper permissions and reinvite the bot.

### 2. Ollama Not Running

- Make sure Ollama is running in a separate terminal window. Start it with:

  ```bash
  ollama serve
  ```

### 3. Missing Packages

- If any packages are missing, ensure your virtual environment is activated and run:

  ```bash
  pip install -r requirements.txt
  ```

### 4. Environment Variables Not Set

- Double-check that your `.env` file includes all necessary tokens (Discord, Gemini, GitHub).
- Ensure you’ve correctly loaded these variables in your bot code.

---

## Contributing

Contributions are welcome! If you’d like to contribute, please fork the repository, make your changes, and submit a pull request. Be sure to follow best practices and include documentation for any new features.

---

## License

This project is licensed under the Apache-2.0 license. See the [LICENSE](LICENSE) file for details.

---

### Notes

- Always keep your bot token and API keys secure. Never share them publicly.
- For development and troubleshooting, you may want to enable logging in your bot’s code to monitor events and errors.

This README provides a complete guide to set up and run StudyBuddy AI, so others can replicate your project smoothly.

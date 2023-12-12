# Byte Buddy

## Introduction

Byte buddy is a personal project introduction to the world of large language model (LLM) api usage and specialized chat bot creation

Byte buddy is meant to be a personal chat bot that a user creates and activates for themself.
In order to explore byte buddy's functionality, please follow the below installation setup

## Installation

Clone the repo onto your local machine and run the following scripts to set up all dependencies

```bash
python -m venv venv

source venv/bin/activate  # On Windows: .\venv\Scripts\activate

mv .env.example .env

pip install -r requirements.txt
```

From here you must go to the telegram messenger client and create a new bot for yourself, to do so,
visit Telegrams "botfather" bot creation chat and run the command /newbot.

Follow the instructions given by the BotFather and save your api token to bytebuddy's .env file as 'TG_BOT_TOKEN'

Next set up an OpenAI account and create an API token for yourself, then save that api token to bytebuddy's .env file as 'OPENAI_API_KEY'

Now you have all dependencies set up and can begin using byte buddy! From the root directory of bytebuddy, simply run 'src/main.py' and go to the URL created and provided to you by the BotFather upon conclusion of making your bot.

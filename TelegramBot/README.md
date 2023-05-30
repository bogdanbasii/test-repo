# WitchBot

This Telegram Bot provides users with their daily horoscope prediction directly to their telegram chat. Users choose their zodiac sign, and the bot will send them a prediction.

## Project Overview

The project has the following structure:

- `run.py`: The main entry point for running the Flask app
- `config.py`: Contains configuration classes for different environments
- `.env`: Contains environment-specific configuration variables
- `/tg_bot`: Contains the main bot module
  - `__init__.py`: Initializes the Flask app and imports views
  - `handlers.py`: Handles the logic of processing incoming Telegram messages
  - `views.py`: Contains Flask route definitions
- `/core`: Consists of core functionality for the bot
  - `__init__.py`: Initializes the Flask app and Flask-Restx API
  - `routes.py`: Defines the API endpoints
  - `utils.py`: Provides utility function for fetching horoscope data

## Installation & Execution

Follow the steps below to set up and run the bot:

1. Clone this repository to your local machine.
2. Use pip to install the project dependencies from `requirements.txt`:
pip install -r requirements.txt
3. Populate your environment variables in the `.env` file.
4. Run ngrok tunnel
ngrok http 4242
5. Run the bot using the command:
python run.py


## How to Use
To use the bot, start a conversation with it on Telegram. The bot will ask for your zodiac sign, and based on your selection, it will provide you with your horoscope prediction.




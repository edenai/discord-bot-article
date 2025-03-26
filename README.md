# Discord Bot with LLM Integration

This project is a Discord bot that uses Retrieval-Augmented Generation (RAG) from EdenAI as a chatbot to respond to users' questions. Built with Python, it leverages the `discord.py` library for Discord interactions and integrates with a Large Language Model (LLM) via EdenAI's API to deliver context-aware, intelligent responses.

## Features

- **Ping Command**: Check the bot's latency with the `!ping` command.
- **Ask Command**: Query the LLM with the `!ask <query>` command to get intelligent responses.
- **Phoenix Integration**: Traces and monitors LLM interactions using the Phoenix library.

## Project Structure

```
.env.example
main.py
phoenix_setup.py
utils.py
```

- `main.py`: The main entry point for the Discord bot.
- `phoenix_setup.py`: Configures Phoenix for tracing and monitoring.
- `utils.py`: Contains utility functions, including the `ask_llm` function for interacting with the LLM API.
- `.env.example`: Example environment variables file.

## Prerequisites

- A Discord bot token
- EDENAI API keys for the LLM
- API TOKEN FOR PHEONIX

## Setup

1. Clone the repository:

2. Install dependencies:

3. Create a `.env` file by copying `.env.example`:

   ```bash
   cp .env.example .env
   ```

4. Fill in the `.env` file with your credentials:

   ```env
   DISCORD_BOT_TOKEN=<your-discord-bot-token>
   RAG_PROJECT_ID=<your-rag-project-id>
   API_KEY=<your-api-key>
   PHOENIX_API_TOKEN=<your-phoenix-api-token>
   PHOENIX_COLLECTOR_ENDPOINT=<your-phoenix-collector-endpoint>
   PHOENIX_CLIENT_HEADERS=api_key=<your-phoenix-client-api-key>
   ```

## Running the Bot

Start the bot by running the following command:

```bash
python main.py
```

## Usage

- **Ping Command**: Type `!ping` in a Discord channel to check the bot's latency.
- **Ask Command**: Type `!ask <your-query>` in a Discord channel to get a response from the LLM.

## Environment Variables

The bot uses the following environment variables:

- `DISCORD_BOT_TOKEN`: Your Discord bot token.
- `RAG_PROJECT_ID`: The project ID for the LLM API.
- `API_KEY`: The API key for the LLM service.
- `PHOENIX_API_TOKEN`: The API token for Phoenix.
- `PHOENIX_COLLECTOR_ENDPOINT`: The endpoint for Phoenix traces.
- `PHOENIX_CLIENT_HEADERS`: Additional headers for Phoenix.

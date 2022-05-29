# DerbyDiscord-Bot
A discord bot for the Derby Discord server.

# Installation
1. [Install Docker](https://docs.docker.com/desktop/linux/install/)
2. Clone this repository and cd into the appropriate directory: `git clone https://github.com/Azelphur/DerbyDiscord-Bot.git && cd DerbyDiscord-bot`
3. Obtain a bot token, and a client token from [here](https://discord.com/developers/applications)
4. Copy `.env.example` to `.env` and insert the bot token.
5. Run `docker compose up -d`
6. Edit this link, replacing CLIENT_TOKEN_HERE with the client token: https://discord.com/api/oauth2/authorize?client_id=CLIENT_TOKEN_HERE&permissions=1506393189456&scope=applications.commands%20bot
7. Visit the link and add the bot to your server.

import discord
import argparse
import logging
import sys
import os
import traceback
from discord.ext import commands
from humanize import naturaldelta

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(
    logging.CRITICAL
)  # set later by set_log_level_from_verbose() in interactive sessions
console_handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(console_handler)
bot = discord.Bot()


@bot.event
async def on_application_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.respond(
            f"This command is on cooldown for {naturaldelta(error.retry_after)}"
        )
        return
    if isinstance(error, commands.CommandError):
        await ctx.respond(error)
        return
    logger.critical(error)
    raise error  # re-raise the error so all the errors will still show up in console


@bot.event
async def on_ready():
    logger.info("Connected to Discord.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Derby Discord bot",
    )
    parser.add_argument(
        "-l",
        "--log-level",
        help="Logging level.",
        choices=["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"],
        default=os.environ.get("BOT_LOG_LEVEL"),
    )
    parser.add_argument(
        "-t",
        "--bot-token",
        type=str,
        help="Discord bot token, or set BOT_TOKEN environment variable.",
        default=os.environ.get("BOT_TOKEN"),
    )
    args = parser.parse_args()

    if not args.bot_token:
        parser.error(
            "Specify any of -t, --bot-token or BOT_TOKEN environment variable."
        )
        sys.exit(1)

    console_handler.setLevel(args.log_level if args.log_level else "INFO")

    cogs_list = [
        "voice_chat",
    ]
    for cog in cogs_list:
        bot.load_extension(f"cogs.{cog}")
    bot.run(args.bot_token)

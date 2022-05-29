import discord
from discord.ext import commands


class VoiceChat(discord.Cog):
    @discord.slash_command(
        name="voicechat",
        description="Ping users to join voice chat",
        cooldown=commands.CooldownMapping.from_cooldown(
            1, 60 * 60, commands.BucketType.guild
        ),
        cooldown_after_parsing=True,
    )
    async def voice_chat(self, ctx):
        role = discord.utils.get(ctx.guild.roles, name="Voice Chat")
        if role is None:
            self.voice_chat.reset_cooldown(ctx)
            raise commands.CommandError(
                "Server misconfigured: Voice Chat role is missing."
            )
        if role not in ctx.author.roles:
            self.voice_chat.reset_cooldown(ctx)
            raise commands.CommandError(
                "You must have the Voice Chat role enabled to use this command. You can get it in #roles."
            )
        await ctx.respond(
            f"{role.mention} {ctx.author.mention} is in voice chat and would like to chat!"
        )


def setup(bot):
    bot.add_cog(VoiceChat(bot))

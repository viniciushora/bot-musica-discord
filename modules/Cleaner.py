from discord.ext import commands

from config.Channels import Channels

class ClearCommands(commands.Cog):

    @commands.Cog.listener("on_message")
    async def delete_commands(self, message):
        if message.author.bot:
            return
        if message.content.startswith(".") or message.content.startswith("-") or message.content.startswith("/"):
            await message.delete()
        elif message.channel.id == Channels.MUSIC_BOT.value:
            await message.delete()


def setup(bot):
    bot.add_cog(ClearCommands(bot))

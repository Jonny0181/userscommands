import discord
from discord.ext import commands

class James:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def james(self, ctx):
        author = ctx.message.author
        e = discord.Embed(description="""**Links:**
Twitch: https://www.twitch.tv/jameschil_l
Twitter: https://twitter.com/JamesChil_l
Discord: https://discord.gg/HU5XzjW

**Clips:**
https://clips.twitch.tv/SavageCreativeElephantBuddhaBar""", colour=author.colour)
        e.set_author(name=author.name, icon_url=author.avatar_url)
        await self.bot.say(embed=e)
        
def setup(bot):
    n = James(bot)
    bot.add_cog(n)

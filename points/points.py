from redbot.core import commands

class Points(commands.Cog):
    """Points"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def points(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

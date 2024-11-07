from discord import app_commands, Interaction  
from discord.ext import commands

async def setup(bot):
    @bot.tree.command(name="ping", description="ping!")
    async def ping(interaction: Interaction):
        await interaction.response.send_message("Pong!")

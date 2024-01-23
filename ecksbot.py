
import discord
from discord import app_commands
def run_slash_cmds():
    TOKEN = 'Insert Discord Ticket Here'

    class aclient(discord.Client):
        def __init__(self):
            super().__init__(intents=discord.Intents.default())
            self.synced = False
        async def on_ready(self):
            await self.wait_until_ready()
            if not self.synced:
                await tree.sync(guild = discord.Object(id = 1000136052931039333))
                self.synced = True
            print(f'Slash command logged in as {self.user}')
    client = aclient()
    tree = app_commands.CommandTree(client)
    @tree.command(name = 'hello', description = 'Says hello to the user', guild = discord.Object(id = 1000136052931039333))
    async def self(interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f'Hello, {name}!', ephemeral = True)
    @tree.command(name = 'witch', description = 'summons a millenial emote for witch', guild = discord.Object(id = 1000136052931039333))
    async def self1(interaction: discord.Interaction, name: str):
        await interaction.response.send_message(f':joy: (insert millenial saying) (I dont know your greetings and such) :rolling_eyes:, brought to you by {name}!', ephemeral = True)
    client.run(TOKEN)
